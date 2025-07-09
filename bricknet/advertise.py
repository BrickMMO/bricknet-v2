import dbus
import dbus.mainloop.glib
import dbus.service
from gi.repository import GLib

from . import config


class Advertise(dbus.service.Object):
    def __init__(self, channel: int, message: str):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        self.loop = None

        self.path = config.DEFAULT_PATH_BASE + str(config.DEFAULT_ADVERTISEMENT_INDEX)
        self.local_name = config.DEFAULT_NAME
        self.payload_bytes = self._create_payload(channel, message)

        super().__init__(self.bus, self.path)

    def _create_payload(self, channel, message):
        payload = bytes([
            channel,
            0,
            (5 << 5) | len(message.encode()),
            *message.encode()
        ])
        return [dbus.Byte(b) for b in payload]

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def get_properties(self):
        return {
            'org.bluez.LEAdvertisement1': {
                'Type': 'peripheral',
                'LocalName': self.local_name,
                'ManufacturerData': dbus.Dictionary({
                    config.DEFAULT_MANUFACTURER_ID: dbus.Array(self.payload_bytes, signature='y')
                }, signature='qv'),
            }
        }

    @dbus.service.method('org.freedesktop.DBus.Properties',
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        return self.get_properties()['org.bluez.LEAdvertisement1']

    @dbus.service.method('org.bluez.LEAdvertisement1',
                         in_signature='',
                         out_signature='')
    def Release(self):
        print('Advertisement released')

    def start(self):
        adapter_path = f'/org/bluez/{config.DEFAULT_ADAPTER_NAME}'
        adapter = self.bus.get_object('org.bluez', adapter_path)
        adapter_props = dbus.Interface(adapter, 'org.freedesktop.DBus.Properties')

        # Optional: auto-power on
        # if not adapter_props.Get('org.bluez.Adapter1', 'Powered'):
        #     adapter_props.Set('org.bluez.Adapter1', 'Powered', dbus.Boolean(1))

        self.ad_manager = dbus.Interface(adapter, 'org.bluez.LEAdvertisingManager1')

        def on_success():
            print("✅ Advertising started")

        def on_error(error):
            print(f"❌ Failed to advertise: {error}")

        self.ad_manager.RegisterAdvertisement(self.get_path(), {},
                                              reply_handler=on_success,
                                              error_handler=on_error)

        self.loop = GLib.MainLoop()
        try:
            self.loop.run()
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        if hasattr(self, 'ad_manager') and self.ad_manager:
            try:
                self.ad_manager.UnregisterAdvertisement(self)
                print("🛑 Advertising stopped")
            except Exception:
                print("⚠️ Could not unregister advertisement")

        self.remove_from_connection()

        if self.loop:
            self.loop.quit()
