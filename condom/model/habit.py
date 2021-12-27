import os
from datetime import datetime
from importlib import import_module
from inspect import isclass
from peewee import *


DB_FILENAME = 'habit.db'

db = SqliteDatabase(DB_FILENAME)

class HabitBaseModel(Model):
    class Meta:
        database = db
        auto_increment=True

class HabitBrowserAddressBarText(HabitBaseModel):
    content = CharField(max_length=8192)
    save_at = DateTimeField()

class HabitBrowserCustomRequest(HabitBaseModel):
    url = CharField(max_length=8192)
    headers = TextField()
    body = TextField(null=True)


def habit_init():
    '''
    初始化习惯数据库
    '''
    
    if not os.path.isfile(DB_FILENAME):
        m = import_module('condom.model.habit')
        habit_models = []
        for k,v  in m.__dict__.items():
            if isclass(v) and issubclass(v, HabitBaseModel) and v != HabitBaseModel:
                habit_models.append(v)
        db.create_tables(habit_models)