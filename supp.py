kv = """

RelativeLayout:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        MDToolbar:
            elevation: 11
            title: "   FLAMES"
            font_style:'H3'
            right_action_items: [["account-search", lambda x: app.name_mean()]]
        ScrollView:

    MDTextField:
        id: person1
        hint_text: "First Person Name"
        mode:"rectangle"
        helper_text: "Name should less then 50 characters"
        helper_text_mode: "on_error"
        max_text_length: 50
        pos_hint: {"center_x":.5,"center_y": .8}
        size_hint:0.600,0.120
        font_size:30




    MDTextField:
        id: person2
        hint_text: "Second Person Name"
        mode:"rectangle"
        helper_text: "Name should less then 50 characters"
        helper_text_mode: "on_error"
        pos_hint: {"center_x":.5,"center_y": .6}
        size_hint:0.600,0.120
        max_text_length: 50
        font_size:30

    MDFillRoundFlatButton:
        id:check
        text:"Check your Relation"
        pos_hint: {"center_x":.5,"center_y": .4}
        padding:"10dp"
        theme_text_color: 'Custom'
        text_color: (1,1,1,1)
        on_press:app.data()
    
    MDRaisedButton:
        text: "Change Theme"
        md_bg_color: 1, 0, 1, 1
        pos_hint: {"center_x":.5,"center_y": .1}
        padding:"10dp"
        on_release:app.show_theme_picker()
    MDFloatingActionButton:
        icon: "whatsapp"
        elevation_normal: 11
        pos_hint: {"center_x":.85,"center_y": .1}
        on_release:app.whatsapp()








"""