from .models import user_field ,task ,relation


def check_user(name ): #done
    temp = user_field.objects.filter(username = name)
    if temp.exists() :
        return False
    else :
        return True

def task_checker (task_name): #done 
    temp = task.objects.filter(task_disc = task_name)
    if temp.exists() :
        return temp
    else :
        temp = task(task_disc = task_name )
        temp.save()
        return task_checker(task_name)
    
def  get_user_x(user_name): #done
    u = user_field.objects.filter(username = user_name ).first()
    return u

def get_task(task_name):
    temp = task.objects.filter(task_disc = task_name).first()
    return temp

def add_task (user_name ,task_name , task_time): # done 
    u = user_field.objects.filter(username = user_name).first()
    t = task_checker(task_name).first()
    p = relation(user_r = u, task_r = t, time = task_time)
    p.save()

def save_user (user_name , date_ob ,first_n ,last_n ,email_a ):#done
    temp =  user_field(username = user_name ,email = email_a ,first_name = first_n ,last_name =  last_n ,date_of_birth = date_ob)
    temp.save() 

def list_of_tasks(user_name ):#done 
    query_data = relation.objects.filter(user_r = get_user_x(user_name))
    list_data = []
    for x in query_data:
        dict = {'task_name' : x.task_r.task_disc , 'time' : x.time}
        list_data.append(dict)
    return list_data
        
def delete_task(user_name ,t_name): #done
    u= (get_user_x(user_name)) 
    t = get_task(t_name)
    relation.objects.filter(user_r = u).filter(task_r = t).delete()

def for_checkbox(len):
    base_str = "ch_box"
    list_c_s = []
    for i in range(1,len+1):
        list_c_s.append(base_str+str(i))
    return list_c_s