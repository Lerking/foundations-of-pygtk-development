#!/usr/bin/python3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_border_width(10)
        self.set_size_request(250, -1)
        # Create all of the necessary widgets and initialize the pop-up menu.
        menu = Gtk.Menu.new()
        eventbox = Gtk.EventBox.new()
        progress = Gtk.ProgressBar.new()
        progress.set_text("Nothing Yet Happened")
        progress.set_show_text(True)
        self.create_popup_menu(menu, progress)
        progress.set_pulse_step(0.05)
        eventbox.set_above_child(False)
        eventbox.connect("button_press_event", self.button_press_event, menu)
        eventbox.add(progress)
        eventbox.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        eventbox.realize()
        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.hbox.pack_start(eventbox, False, False, 5)
        self.add(self.hbox)

    def create_popup_menu(self, menu, progress):
        pulse = Gtk.MenuItem.new_with_label("Pulse Progress")
        fill = Gtk.MenuItem.new_with_label("Set as Complete")
        clear = Gtk.MenuItem.new_with_label("Clear Progress")
        separator = Gtk.SeparatorMenuItem.new()
        pulse.connect("activate", self.pulse_activated, progress)
        fill.connect("activate", self.fill_activated, progress)
        clear.connect("activate", self.clear_activated, progress)
        menu.append(pulse)
        menu.append(separator)
        menu.append(fill)
        menu.append(clear)
        menu.attach_to_widget(progress, None)
        menu.show_all()

    def button_press_event(self, eventbox, event, menu):
        pass

    def pulse_activated(self, item, progress):
        pass

    def fill_activated(self, item, progress):
        pass

    def clear_activated(self, item, progress):
        pass

    def on_cutstandard(self, widget):
        pass

    def on_copystandard(self, widget):
        pass

    def on_pastestandard(self, widget):
        pass


class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, 
                                    title="Exercise 1")
            builder = Gtk.Builder()
            builder.add_from_file("./Exercise_1_Toolbar.xml")
            builder.connect_signals(self.window)
            toolbar = builder.get_object("toolbar")
            toolbar.set_orientation(Gtk.Orientation.VERTICAL)
            self.window.hbox.pack_end(toolbar, True, False, 1)
        self.window.show_all()
        self.window.present()

    def on_newstandard(self, widget):
        pass

    def on_openstandard(self, widget):
        pass

    def on_savestandard(self, widget):
        pass


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)
