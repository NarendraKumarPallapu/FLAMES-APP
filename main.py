from kivymd.app import MDApp
from kivy.lang.builder import Builder
from supp import kv
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from kivy.config import Config
from kivymd.uix.picker import MDThemePicker
import webbrowser

Config.set('graphics','resizable', True)

class flames(MDApp):

    def build(self):
        #self.theme_cls.primary_palette="Green"
        return Builder.load_string(kv)



    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()



    def data(self):




        def remove_match_char(list1, list2):
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        c = list1[i]
                        list1.remove(c)
                        list2.remove(c)
                        list3 = list1 + ["*"] + list2
                        return [list3, True]
            list3 = list1 + ["*"] + list2
            return [list3, False]
        p1 = self.root.ids.person1.text
        p1 = p1.lower()
        p1.replace(" ", "")
        p1_list = list(p1)

        p2 = self.root.ids.person2.text
        p2 = p2.lower()
        p2.replace(" ", "")
        p2_list = list(p2)

        proceed = True
        if len(p1_list)==0 and len(p2_list)==0:
            toast("Please Enter both the Names")
        else:
            while proceed:
                ret_list = remove_match_char(p1_list, p2_list)
                con_list = ret_list[0]
                proceed = ret_list[1]
                star_index = con_list.index("*")
                p1_list = con_list[:star_index]
                p2_list = con_list[star_index + 1:]
            count = len(p1_list) + len(p2_list)
            result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

            while len(result) > 1:
                split_index = (count % len(result) - 1)
                if split_index >= 0:
                    right = result[split_index + 1:]
                    left = result[:split_index]
                    result = right + left
                else:
                    result = result[:len(result) - 1]

            toast("You Both are "+result[0])
            #close_result= MDRaisedButton(text='Close')
            dialog=MDDialog(title="Your Relationship is "+str(result[0]),size_hint=(0.4,0))
            dialog.open()

    def whatsapp(self):
        webbrowser.open("https://api.whatsapp.com/send?text=")
    def name_mean(self):
        webbrowser.open("https://www.behindthename.com/")











flames().run()