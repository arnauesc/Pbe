import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Puzzle2(Gtk.Window):
    def __init__(self):
        super().__init__(title = "Puzzle 2")
        self.set_default_size(300,80)
        self.set_border_width(8)
        self.uid=""
        
        self.blue = b""" 
                
        #label1{
            background-color: #29c8f6;
            font: bold 24px Calibri;
            color:#FFFFFF;
            }
               
        """
        self.red = b"""
        
         #label1{
            background-color: #dd1432;
            font: bold 24px Calibri;
            color: #FFFFFF;
            }
        """
        
        self.css_provider = Gtk.CssProvider() #Adding styles
        self.css_provider.load_from_data(self.blue) 
        self.context = Gtk.StyleContext()
        self.screen = Gdk.Screen.get_default()
        self.context.add_provider_for_screen(self.screen, self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        #Es crea la finestra, ajustant les dimensions
        
        
        #creem una caixa i l'afegim a la finestra
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add(self.box)
        
        #Es crea una caixa eventual
        self.event1 = Gtk.EventBox()
        
        
        #Creem una etiqueta que l'afegim a la caixa eventual
        self.label = Gtk.Label()
        self.label.set_name("label1")
        self.label.set_text("Please log with yout university card")
        self.label.set_use_markup(True)
        self.box.pack_start(self.label,True,True,0)
        
        
        #Creem un boto clear i l'afegim a la caixa
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicat)
        self.button.set_can_focus(False)
        self.event1.add(self.button)
        self.box.pack_start(self.event1, True, True,0)
        
        
        self.connect("key_press_event",self.scan)
        
    
    def clicat(self, boto):
    
        self.label.set_text("Please log with yout university card")
        self.css_provider.load_from_data(self.blue)
        
        
        
    def scan(self,widget, event):
        
        if(Gdk.keyval_name(event.keyval) == "Return"):
            self.big_endian_to_little_endian_string()
            self.box.set_name("box2")
            self.label.set_text("UID: " + self.uid)
            self.uid = ""
        else:
            self.uid = self.uid + Gdk.keyval_name(event.keyval)

        self.css_provider.load_from_data(self.red)
    def big_endian_to_little_endian_string(self):
        self.uid= hex(int(self.uid))[2:]
        self.uid = bytearray.fromhex(self.uid)[::-1].hex().upper()
        
        
if __name__ == "__main__":
    fin = Puzzle2()
    fin.connect("destroy", Gtk.main_quit)
    fin.show_all()
    Gtk.main()
        
        