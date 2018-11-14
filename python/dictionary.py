my_dict = {}
>>> my_dict
{}
>>> my_dict = {"id":123, "name":"manju", "age":22}
>>> my_dict
{'age': 22, 'id': 123, 'name': 'manju'}
>>> my_dict = {"name":"ann","place
  File "<stdin>", line 1
    my_dict = {"name":"ann","place
                                 ^
SyntaxError: EOL while scanning string literal
>>> my_dict = {"name":"ann","place":"kasaragod"}
>>> my_dict
{'place': 'kasaragod', 'name': 'ann'}
>>> my_dict = {"id":123, "name":"manju", "age":22,[1,2]:"numbers"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> dict_1 = {"name":"anju","age":23,"name":"arya"}
>>> dict_1
{'age': 23, 'name': 'arya'}
>>> my_dict = {1: 'apple', 2: 'ball'}
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> my_dict = {'name': 'manju', 1: [2,4,3]}
>>> my_dict
{1: [2, 4, 3], 'name': 'manju'}
>>> my_dict = {'name':'manju', 'age':22}
>>> my_dict
{'age': 22, 'name': 'manju'}
>>> my_dict = {'name :'manju',
  File "<stdin>", line 1
    my_dict = {'name :'manju',
                           
>>> my_dict = {'name':'manju', 'age':22}
>>> my_dict
{'age': 22, 'name': 'manju'}
>>> my_dict = {'name':'anju','place':'kollam','age':22}
>>> my_dict
{'age': 22, 'place': 'kollam', 'name': 'anju'}
>>> my_dict[name] = 'anu'
>>> my_dict[name] = 'anu'
>>> my_dict = {'name':'anju','place':'kollam','age':22}
>>> my_dict
{'age': 22, 'place': 'kollam', 'name': 'anju'}
>>> my_dict['name'] = "anu"
>>> my_dict
{'age': 22, 'place': 'kollam', 'name': 'anu'}
>>> my_dict = {'name':'anju','place':'kollam','age':22}
>>> my_dict
{'age': 22, 'place': 'kollam', 'name': 'anju'}
>>> del my_dict['age']
>>> my_dict
{'place': 'kollam', 'name': 'anju'}
>>> my_dict = {'id':123,'name':"manju"}
>>> len(my_dict)
2
>>> my_dict
{'id': 123, 'name': 'manju'}
>>> {'age':22, 'id':123, 'name':'manju'}
{'age': 22, 'id': 123, 'name': 'manju'}
>>> str(my_dict)
"{'id': 123, 'name': 'manju'}"
>>> my_dict.keys()
['id', 'name']
>>> dict_keys(['age','id',;name'])
  File "<stdin>", line 1
    dict_keys(['age','id',;name'])
                          ^
>>> my_dict.keys()
['id', 'name']
>>> my_dict.values()
[123, 'manju']
>>> my_dict.items()
[('id', 123), ('name', 'manju')]
>>> my_dict = {'id':123,'name':"manju"}

