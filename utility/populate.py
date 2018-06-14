import os.path
import sys
import random
import string

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def create_password():
    '''
    Generates passwords for each user
    '''

    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
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
        print('username: {0} -- password: {1} \n'.format(username, password))

        return u

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_user(first_name, last_name, name, username, email, birthday, gender):
    """
    Creates the user and ensures that if any error occurs the
    script does not continue
    """
    password = create_password()
    if gender == 'F':
        g = 'Female'
    else:
        g = 'Male'
    try:
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            name=name,
            username=username,
            email=email,
            password=password,
            birthday=birthday,
            telephone='(22)22222-2222',
            gender=g,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            is_active=True,
            has_specialization=False
        )

        # EmailAdress is for validating email confirmation on user creation
        EmailAddress.objects.create(
            user=u, email=email,
            primary=True, verified=True)
        u.save()

        print('User: - {0} {1}'.
              format(str(u.first_name), str(u.last_name)))
        print('username: {0}  -- password: {1} \n'.format(username, password))

        return u

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_patient(user, n, responsible):
    try:
        patients = Patient.objects.create(
            ses='11234561' + str(n),
            user=user,
            mother_name="Janaína Roussef",
            father_name="João das neves",
            ethnicity=3,
            sus_number='1234567891' + str(n),
            civil_registry_of_birth='1234567891' + str(n),
            declaration_of_live_birth='1234567891' + str(n),
            responsible=responsible
        )

        Risk.objects.filter(patient=patients).update(
            patient=patients,
            priority_speech_theraphy=5,
            priority_psychology=5,
            priority_physiotherapy=5,
            priority_neurology=5,
            priority_cardiology=5,
            priority_pediatrics=5,
            priority_general_practitioner=5,
        )

        create_curves(patients)

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_healthteam(user, cpf, speciality, council_acronym, register_number):
    try:
        HealthTeam.objects.create(
            cpf=cpf,
            user=user,
            speciality=speciality,
            council_acronym=council_acronym,
            register_number=register_number,
            registration_state=HealthTeam.DF,
        )
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_responsible(user, cpf):
    try:
        responsible = Responsible.objects.create(
            cpf=cpf,
            user=user
        )
        return responsible

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_employee(user, cpf):
    try:
        Employee.objects.create(
            cpf=cpf,
            user=user,
            departament=Employee.ADMINISTRATION
        )
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_curves(patient):
    max_age = random.randint(1, 18 * 12)
    in_range = (max_age * 3) / 4

    weights = [2, ]
    heights = [45, ]
    perimeters = [35, ]

    for age in range(1, max_age):

        skip = random.randint(0, 2)

        if age <= in_range:

            if not skip:
                weight = random.randint(
                    max(weights), max(weights) + random.randint(1, 2)
                )
                weights.append(weight)

                height = random.randint(
                    max(heights), max(heights) + random.randint(2, 5)
                )
                heights.append(height)

                perimeter = random.randint(
                    max(perimeters), max(perimeters) + random.randint(0, 3)
                )
                perimeters.append(perimeter)

                Curves.objects.create(
                    patient=patient,
                    weight=weight,
                    height=height,
                    age=age,
                    cephalic_perimeter=perimeter,
                )

        else:

            if not skip:
                weight = random.randint(
                    max(weights), max(weights) + random.randint(1, 1)
                )
                weights.append(weight)

                height = random.randint(
                    max(heights), max(heights) + random.randint(1, 3)
                )
                heights.append(height)

                perimeter = random.randint(
                    max(perimeters), max(perimeters) + random.randint(0, 2)
                )
                perimeters.append(perimeter)

                Curves.objects.create(
                    patient=patient,
                    weight=weight,
                    height=height,
                    age=age,
                    cephalic_perimeter=perimeter,
                )


def populate():
    print ('\n----------------------')
    print ('Populating Database...')
    print ('----------------------\n')

    create_super_user('admin', 'admin@admin.com')

    print ('\n------------------------')
    print ('Creating Health Teams...')
    print ('------------------------\n')

    healthteam_1 = create_user(
        'Laura',
        'Oliveira',
        'Laura Oliveira',
        'laura',
        'laura@email.com',
        '1998-04-05',
        'F'
    )

    healthteam_2 = create_user(
        'Maura',
        'Oliveira',
        'Maura Oliveira',
        'maura',
        'maura@email.com',
        '1998-04-05',
        'F'
    )

    healthteam_3 = create_user(
        'Sara',
        'Oliveira',
        'Sara Oliveira',
        'sara',
        'sara@email.com',
        '1998-04-05',
        'F'
    )

    healthteam_4 = create_user(
        'Diogo',
        'Thiago',
        'Diogo Thiago',
        'diogo',
        'diogo@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_4,
        '756.750.559-24',
        HealthTeam.SPEECH_THERAPHY,
        HealthTeam.CREFONO,
        1234548
    )

    healthteam_5 = create_user(
        'Marcelo',
        'Filipe',
        'Marcelo Filipe',
        'marcelo',
        'marcelo@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_5,
        '395.183.589-31',
        HealthTeam.PSYCHOLOGY,
        HealthTeam.CRP,
        1234578
    )

    healthteam_6 = create_user(
        'Heitor',
        'Ian',
        'Heitor Ian',
        'heitor',
        'heitor@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_6,
        '227.707.358-02',
        HealthTeam.PHYSIOTHERAPY,
        HealthTeam.CREFITO,
        1234448
    )

    healthteam_7 = create_user(
        'Gustavo',
        'Roberto',
        'Gustavo Roberto',
        'gustavo',
        'gustavo@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_7,
        '914.049.996-04',
        HealthTeam.OCCUPATIONAL_THERAPY,
        HealthTeam.CREFITO,
        1235548
    )

    healthteam_8 = create_user(
        'Fábio',
        'Rodrigo',
        'Fábio Rodrigo',
        'fabio',
        'fabio@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_8,
        '627.696.105-11',
        HealthTeam.GENERAL_PRACTITIONER,
        HealthTeam.CRM,
        2235548
    )

    healthteam_9 = create_user(
        'Emanuel',
        'Henry',
        'Emanuel Henry',
        'emanuel',
        'emanuel@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_9,
        '271.770.958-45',
        HealthTeam.CARDIOLOGY,
        HealthTeam.CRM,
        1735548
    )
    healthteam_10 = create_user(
        'Renato',
        'Jorge',
        'Renato Jorge',
        'renato',
        'renato@email.com',
        '1998-04-05',
        'M'
    )
    create_healthteam(
        healthteam_10,
        '002.213.483-28',
        HealthTeam.PEDIATRICS,
        HealthTeam.CRM,
        1775548
    )

    create_healthteam(
        healthteam_1,
        '326.763.330-38',
        HealthTeam.NEUROLOGY,
        HealthTeam.CRM,
        1234567
    )
    create_healthteam(
        healthteam_2,
        '875.076.060-23',
        HealthTeam.NURSING,
        HealthTeam.COREN,
        1234568
    )
    create_healthteam(
        healthteam_3,
        '452.347.400-13',
        HealthTeam.NEUROLOGY,
        HealthTeam.CRM,
        1234569
    )

    print ('\n------------------------')
    print ('Creating Responsibles...')
    print ('------------------------\n')

    responsible_1 = create_user(
        'José',
        'Vaz',
        'José Vaz',
        'jose',
        'jose@email.com',
        '1998-04-05',
        'M'
    )

    responsible_2 = create_user(
        'Ana',
        'Vitória',
        'Ana Vitória',
        'ana',
        'ana@email.com',
        '1998-04-05',
        'F'
    )

    responsible_3 = create_user(
        'Júlio',
        'Tavares',
        'Júlio Tavares',
        'julio',
        'julio@email.com',
        '1998-04-05',
        'M'
    )

    responsible1 = create_responsible(responsible_1, "902.876.510-70")
    responsible2 = create_responsible(responsible_2, "715.643.220-68")
    responsible3 = create_responsible(responsible_3, "445.821.390-35")

    print ('\n----------------------')
    print ('Creating Patients...')
    print ('----------------------\n')

    print ('(Minnor)')
    patient_3 = create_user(
        'Enzo',
        'Gabriel',
        'Enzo Gabriel',
        'enzo',
        'enzo@email.com',
        timezone.now() - timezone.timedelta(days=3650),
        'M',
    )

    print ('(Minnor)')
    patient_4 = create_user(
        'Valentina',
        'Valente',
        'Valentina Valente',
        'valentina',
        'valentina@email.com',
        timezone.now() - timezone.timedelta(days=1),
        'F'
    )

    print ('(18+)')
    patient_1 = create_user(
        'Gabriel',
        'dos Santos',
        'Gabriel dos Santos',
        'gabriel',
        'gabriel@email.com',
        '1998-04-05',
        'M'
    )

    print ('(18+)')
    patient_2 = create_user(
        'Carla',
        'Júlia',
        'Carla Júlia',
        'carla',
        'carla@email.com',
        '1998-04-05',
        'F'
    )

    print ('(Minnor)')
    patient_5 = create_user(
        'Bia',
        'Falcão',
        'Bianca Falcão',
        'bianca',
        'bianca@email.com',
        timezone.now() - timezone.timedelta(days=1),
        'F'
    )

    print ('(18+)')
    patient_6 = create_user(
        'Nathan',
        'Vilela',
        'Nathan Vilela',
        'nathan',
        'nathan@email.com',
        '1998-04-05',
        'M'
    )

    create_patient(patient_3, 3, responsible1)
    create_patient(patient_4, 4, responsible2)
    create_patient(patient_5, 5, responsible2)
    create_patient(patient_6, 6, responsible2)
    create_patient(patient_1, 1, None)
    create_patient(patient_2, 2, None)

    print ('\n------------------------')
    print ('Creating Employees...')
    print ('------------------------\n')

    employee_1 = create_user(
        'Pedro',
        'Victor',
        'Pedro Victor',
        'pedro',
        'pedro@email.com',
        '1998-04-05',
        'M'
    )

    employee_2 = create_user(
        'Raíssa',
        'Parente',
        'Raíssa Parente',
        'raissa',
        'raissa@email.com',
        '1998-04-05',
        'F'
    )

    create_employee(employee_1, "112.954.800-77")
    create_employee(employee_2, "832.164.830-45")

    category1 = Category.objects.create(
        name='Medicamentos',
        description='Fórum de discussão sobre medicamentos',
        slug='med',
    )

    post1 = Post.objects.create(
        title="Qual medicamento tomar?",
        message="Tenho dores de cabeça",
        created_by=patient_1,
        category=category1,
    )

    Commentary.objects.create(
        message='Gostaria de saber também',
        post=post1,
        created_by=patient_2,
    )

    category2 = Category.objects.create(
        name='Espaço dos pais',
        description='Um lugar para os pais discutirem e trocarem infrmações',
        slug='event',
    )

    post2 = Post.objects.create(
        title="Meu filho não tá legal",
        message="Ele não fala com ninguém. É normal?",
        created_by=responsible_1,
        category=category2,
    )

    Commentary.objects.create(
        message='O meu conversa com os amigos normalmente. Veja com um médico.',
        post=post2,
        created_by=responsible_2,
    )

    category3 = Category.objects.create(
        name='Dúvidas',
        description='Espaço de dúvidas',
        slug='event',
    )

    post3 = Post.objects.create(
        title="Onde achar um bom site sobre SD?",
        message="Gostaria de achar um site muito bom sobre SD",
        created_by=employee_1,
        category=category3,
    )

    Commentary.objects.create(
        message='Você está nele :D',
        post=post3,
        created_by=employee_2,
    )

    event_1 = Events.objects.create(
        name="Festival de Halloween",
        location="HRAN",
        date="2018-10-31",
        time="16:20",
        description="Venha aproveitar com a sua família.",
        organize_by="Cris Down",
        free=False,
        value=40.00,
    )

    event_2 = Events.objects.create(
        name="Palestra sobre Síndrome de Down",
        location="HRAN",
        date="2018-10-10",
        time="08:10",
        description="A palestra alertará sobre os procedimentos necessários.",
        organize_by="Cris Down",
        free=False,
        value=10.00,
    )

    event_3 = Events.objects.create(
        name="Palestra sobre Vacinas",
        location="HRAN",
        date="2018-10-15",
        time="15:00",
        description="A palestra falará sobre o calendário de vacinas.",
        organize_by="Cris Down",
        free=True,
        value=0,
    )

    print ('================================================================')
    print ('WARNING:\n')
    print ('All passwords displayed on this terminal '
           'are generated randomly\n and can not be '
           'displayed again. Be sure to save them in '
           'a safe \nplace before continuing, otherwise'
           'you will have to redo the whole\n process.')
    print ('================================================================\n')

    input("I saved the passwords in a safe place (press enter to continue...)")

    print ('\n------------------------------\n')
    print ('Database populated with sucess')
    print ('------------------------------\n')


import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from django.utils import timezone
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from drdown.medicalrecords.models.model_curves import Curves
from drdown.forum.models.model_category import Category
from drdown.forum.models.model_post import Post
from drdown.events.models.model_events import Events
from drdown.forum.models.model_commentary import Commentary
from drdown.medicalrecords.models.model_risk import Risk
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from allauth.account.models import EmailAddress

populate()
