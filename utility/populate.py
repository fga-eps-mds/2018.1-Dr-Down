import os.path
import sys
import random
import string

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def create_password():
    '''
    Generates random passwords for each user
    '''

    password = ''.join(random.choice(string.ascii_uppercase +
                                     string.ascii_lowercase +
                                     string.digits) for _ in range(9)
                       )
    return password


def create_super_user(username, email):
    '''
    Creates the superuser and ensures that if any error occurs the
    script does not continue
    '''

    password = create_password()
    try:
        u = User.objects.create_superuser(username,
                                          email,
                                          password,
                                          is_active=True)
        EmailAddress.objects.create(
            user=u, email=email,
            primary=True, verified=True)
        u.set_password(password)
        u.save()
        print ('\nSuperUser:', User.objects.get(is_superuser=True).username)
        print('username: {0} -- password: {1} \n'. format(username, password))

        return u
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_user(first_name, last_name, name, username, email, birthday):
    """
    Creates the user and ensures that if any error occurs the
    script does not continue
    """
    password = create_password()
    try:
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            name=name,
            username=username,
            email=email,
            password=password,
            birthday='1998-04-05',
            telephone='(22)22222-2222',
            gender='M',
            created_at='2018-04-05',
            updated_at='2018-04-05',
            is_active=True,
        )

        # EmailAdress is for validating email confirmation on user creation
        EmailAddress.objects.create(
            user=u, email=email,
            primary=True, verified=True)
        u.save()

        print('User: - {0} {1}'.
              format(str(u.first_name), str(u.last_name)))
        print('username: {0}  -- password: {1} \n'. format(username, password))

        return u
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def populate():

    print ('\n----------------------')
    print ('Populating Database...')
    print ('----------------------\n')

    create_super_user('admin', 'admin@admin.com')

    user_employee = create_user(
        'Pedro',
        'Victor',
        'Pedro',
        'pedro',
        'pedro@gmail.com',
        '1998-04-05',
    )

    user_patient = create_user(
        'Enzo',
        'Gabriel',
        'Enzo',
        'enzo',
        'enzo@gmail.com',
        '1998-04-05',
    )

    user_responsible = create_user(
        'Maria',
        'Joaquina',
        'Maria',
        'maria',
        'maria@gmail.com',
        '1998-04-05',
    )

    user_healthteam = create_user(
        'Laura',
        'Nsei',
        'Laura',
        'laura',
        'laura@gmail.com',
        '1998-04-05',
    )

    user_patient_with_responsible = create_user(
        'Huiller',
        'Victor',
        'Huiller',
        'huiller',
        'huiller@gmail.com',
        '1998-04-05',
    )

    user_test = create_user(
        'teste',
        'teste',
        'teste',
        'teste',
        'teste@gmail.com',
        '1998-04-05',
    )

    Employee.objects.create(
        cpf="974.220.200-16",
        user=user_employee,
        departament=Employee.ADMINISTRATION
    )

    HealthTeam.objects.create(
        cpf="057.641.271-65",
        user=user_healthteam,
        speciality=HealthTeam.NEUROLOGY,
        council_acronym=HealthTeam.CRM,
        register_number="1234567",
        registration_state=HealthTeam.DF,
    )

    Patient.objects.create(
        ses="1234567",
        user=user_patient,
        priority=1,
        mother_name="Mãe",
        father_name="Pai",
        ethnicity=3,
        sus_number="12345678911",
        civil_registry_of_birth="12345678911",
        declaration_of_live_birth="12345678911"
    )

    responsible = Responsible.objects.create(
        cpf="914.479.730-38",
        user=user_responsible
    )

    Patient.objects.create(
        ses="1234568",
        user=user_patient_with_responsible,
        responsible=responsible,
        priority=1,
        mother_name="Mãe",
        father_name="Pai",
        ethnicity=3,
        sus_number="12345678912",
        civil_registry_of_birth="12345678912",
        declaration_of_live_birth="12345678912"
    )

    category1 = Category.objects.create(
        name='Medicamentos',
        description='Fórum de discussão sobre medicamentos',
        slug='med',

    )

    category2 = Category.objects.create(
        name='Espaço dos pais',
        description='Um lugar para os pais discutirem e trocarem infrmações',
        slug='event',
    )

    print ('------------------------------\n')
    print ('Database populated with sucess')
    print ('------------------------------\n')


import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from drdown.forum.models.model_category import Category
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from allauth.account.models import EmailAddress

populate()
