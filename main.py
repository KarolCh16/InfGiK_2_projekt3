from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import shuffle
from Vincent import vincent
global points, counts




points = [
                ['paris.jpg', 48.8582602, 2.29449905431968],
                ['london.jpg', 51.50069, -0.124583917963503],
                ['warsaw.jpg', 52.2317641, 21.0057996756161],
                ['berlin.jpg', 52.51628045, 13.3777018828817],
                ['prague.jpg', 50.0870353, 14.4077757],
                ['moscow.jpg', 55.7514952, 37.6181737535743],
                ['rome.jpg', 41.890200056842964, 12.492342711902083],
                ['athens.jpg', 37.9715141, 23.7266498463072],
                ['amsterdam.jpg', 52.3745403, 4.89797550561798],
                ['barcelona.jpg', 41.4034789, 2.17441033300971]
        ]
shuffle(points)
counts=len(points)
class Form(BoxLayout):   
    def draw_marker(self):
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{:.5f}".format(self.latitude)
        self.search_long.text = "{:.5f}".format(self.longitude)
        
    def check_points(self):
        a = 6378137.000
        e2 = 0.00669438002290
        Az1, Az2, s = vincent(self.curr_img[1], self.curr_img[2], self.latitude, self.longitude, a, e2)

        
        if self.my_image.source in ['welcome.jpg','the end.jpg']:
            pass
        else:
            if 0<=s<=3000:
                self.my_score.text=str(int(self.my_score.text)+5)
                self.my_button_check.disabled = True
            elif 3000<s<=6000:
                self.my_score.text=str(int(self.my_score.text)+4)
                self.my_button_check.disabled = True
            elif 6000<s<=9000:
                self.my_score.text=str(int(self.my_score.text)+3)
                self.my_button_check.disabled = True
            elif 9000<s<=14000:
                self.my_score.text=str(int(self.my_score.text)+2)
                self.my_button_check.disabled = True
            elif 14000<s<=20000:
                self.my_score.text=str(int(self.my_score.text)+1)
                self.my_button_check.disabled = True
            else:
                self.my_button_check.disabled = True
        
            
        
                
    def next_img(self):
        self.my_button_check.disabled = False
        if len(points)>=1:
            self.curr_img=points.pop()
            self.my_image.source = self.curr_img[0]
            self.my_button_next.text='NEXT'
        else:
            self.my_image.source = 'the end.jpg'
            self.my_button_next.disabled = True
            self.my_button_check.disabled = True
            self.my_button_next.text='END'
    
         
        


class MapViewApp(App):
    pass

MapViewApp().run()