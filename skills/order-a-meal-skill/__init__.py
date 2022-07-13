from mycroft import MycroftSkill, intent_file_handler
import re

def whichmeal():
    import datetime
    now = datetime.datetime.now()
    hour = float(now.hour) + float(now.minute) / 60.0
    mealmap = [
        {"start": 5, "end": 10.5, "mealname": "breakfast"},
        {"start": 11.5, "end": 13.5, "mealname": "lunch"},
        {"start": 17, "end": 20, "mealname": "supper"}
    ]
    for meal in mealmap:
        if hour >= meal['start'] and hour < meal['end']:
            return meal['mealname']
    
    return "snack"

class OrderAMeal(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.register_entity_file('foodtype.entity')
        self.register_entity_file('mealname.entity')

    @intent_file_handler('meal.a.order.intent')
    def handle_meal_a_order(self, message):
        self.log.info("\n\nORDER A MEAL INVOKED WITH %s\n\n", repr(message.data))
        if re.sub(r'[^a-zA-Z\s]+', ' ', message.data.get('utterance')).startswith("timed entry order meal"):
            mealname = whichmeal()
            foodtype = self.get_response('hey.dan.time.to.eat.what.do.you.want.for.'+mealname)
        else:
            foodtype = message.data.get('foodtype')
            mealname = message.data.get('mealname')
            if not mealname:
                mealname = whichmeal()
        
        if not foodtype:
            foodtype = self.get_response('please.tell.me.what.you.would.like.for.'+mealname)
            
        self.speak_dialog('order.confirmation', data={
            'mealname': mealname,
            'foodtype': foodtype
        })



def create_skill():
    return OrderAMeal()
    