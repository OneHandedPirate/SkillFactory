from GuestsList import NewGuests

personnel_collection = {}
collection = []

while True:
    full_name = input('Введите имя: ')
    city = input('Введите город: ')
    status = input('Введите роль сотрудника: ')
    print('Введите "stop", если хотите завершить заполнение списка')
    personnel_collection['full_name'] = full_name
    personnel_collection['city'] = city
    personnel_collection['status'] = status

    collection.append(personnel_collection.copy())
    a = input()
    if a.lower() == 'stop':
        break

for guest in collection:
    guest_person = NewGuests()
    guest_person.init_from_dict(guest)
    print(f'{guest_person.full_name},', f'г.{guest_person.city},', f'статус "{guest_person.status}"')
