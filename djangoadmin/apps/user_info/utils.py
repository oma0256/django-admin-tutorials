from faker import Faker


def generate_user_info_data(gender):
    fake = Faker()
    user_info = {}
    user_info['username'] = fake.user_name()
    user_info['gender'] = gender
    user_info['first_name'] = fake.first_name_male() if gender == 'M' else fake.first_name_female()
    user_info['last_name'] = fake.last_name_male() if gender == 'M' else fake.last_name_female()
    user_info['email'] = fake.email()
    user_info['company'] = fake.company()
    user_info['address'] = fake.address()
    user_info['country'] = fake.country()
    user_info['phone_number'] = fake.phone_number()
    return user_info


def duplicate_model_instance(instance):
    instance.pk = None
    return instance.save()
