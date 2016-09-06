import emoji
import random

from faker import Faker


fake = Faker()

CATEGORIES = ( 'general', 'eating_out', 'expenses', 'transport', 'cash',
'bills', 'entertainment', 'shopping', 'holidays', 'groceries', )

EMOJI = ( ':bamboo:', ':gift_heart:', ':dolls:', ':school_satchel:',
':mortar_board:', ':flags:', ':fireworks:', ':sparkler:', ':wind_chime:',
':rice_scene:', ':jack_o_lantern:', ':ghost:', ':santa:', ':christmas_tree:',
':gift:', ':bell:', ':no_bell:', ':tanabata_tree:', ':tada:', ':confetti_ball:',
':balloon:', ':crystal_ball:', ':cd:', ':dvd:', ':floppy_disk:', ':camera:',
':video_camera:', ':movie_camera:', ':computer:', ':tv:', ':iphone:', ':phone:',
':telephone:', ':telephone_receiver:', ':pager:', ':fax:', ':minidisc:',
':vhs:', ':sound:', ':speaker:', ':mute:', ':loudspeaker:', ':mega:',
':hourglass:', ':hourglass_flowing_sand:', ':alarm_clock:', ':watch:',
':radio:', ':satellite:', ':loop:', ':mag:', ':mag_right:', ':unlock:',
':lock:', ':lock_with_ink_pen:', ':closed_lock_with_key:', ':key:', ':bulb:',
':flashlight:', ':high_brightness:', ':low_brightness:', ':electric_plug:',
':battery:', ':calling:', ':email:', ':mailbox:', ':postbox:', ':bath:',
':bathtub:', ':shower:', ':toilet:', ':wrench:', ':nut_and_bolt:', ':hammer:',
':seat:', ':moneybag:', ':yen:', ':dollar:', ':pound:', ':euro:',
':credit_card:', ':money_with_wings:', ':e-mail:', ':inbox_tray:',
':outbox_tray:', ':envelope:', ':incoming_envelope:', ':postal_horn:',
':mailbox_closed:', ':mailbox_with_mail:', ':mailbox_with_no_mail:',
':package:', ':door:', ':smoking:', ':bomb:', ':gun:', ':hocho:', ':pill:',
':syringe:', ':page_facing_up:', ':page_with_curl:', ':bookmark_tabs:',
':bar_chart:', ':chart_with_upwards_trend:', ':chart_with_downwards_trend:',
':scroll:', ':clipboard:', ':calendar:', ':date:', ':card_index:',
':file_folder:', ':open_file_folder:', ':scissors:', ':pushpin:', ':paperclip:',
':black_nib:', ':pencil2:', ':straight_ruler:', ':triangular_ruler:',
':closed_book:', ':green_book:', ':blue_book:', ':orange_book:', ':notebook:',
':notebook_with_decorative_cover:', ':ledger:', ':books:', ':bookmark:',
':name_badge:', ':microscope:', ':telescope:', ':newspaper:', ':football:',
':basketball:', ':soccer:', ':baseball:', ':tennis:', ':8ball:',
':rugby_football:', ':bowling:', ':golf:', ':mountain_bicyclist:',
':bicyclist:', ':horse_racing:', ':snowboarder:', ':swimmer:', ':surfer:',
':ski:', ':spades:', ':hearts:', ':clubs:', ':diamonds:', ':gem:', ':ring:',
':trophy:', ':musical_score:', ':musical_keyboard:', ':violin:',
':space_invader:', ':video_game:', ':black_joker:', ':flower_playing_cards:',
':game_die:', ':dart:', ':mahjong:', ':clapper:', ':memo:', ':pencil:',
':book:', ':art:', ':microphone:', ':headphones:', ':trumpet:', ':saxophone:',
':guitar:', ':shoe:', ':sandal:', ':high_heel:', ':lipstick:', ':boot:',
':shirt:', ':tshirt:', ':necktie:', ':womans_clothes:', ':dress:',
':running_shirt_with_sash:', ':jeans:', ':kimono:', ':bikini:', ':ribbon:',
':tophat:', ':crown:', ':womans_hat:', ':mans_shoe:', ':closed_umbrella:',
':briefcase:', ':handbag:', ':pouch:', ':purse:', ':eyeglasses:',
':fishing_pole_and_fish:', ':coffee:', ':tea:', ':sake:', ':baby_bottle:',
':beer:', ':beers:', ':cocktail:', ':tropical_drink:', ':wine_glass:',
':fork_and_knife:', ':pizza:', ':hamburger:', ':fries:', ':poultry_leg:',
':meat_on_bone:', ':spaghetti:', ':curry:', ':fried_shrimp:', ':bento:',
':sushi:', ':fish_cake:', ':rice_ball:', ':rice_cracker:', ':rice:', ':ramen:',
':stew:', ':oden:', ':dango:', ':egg:', ':bread:', ':doughnut:', ':custard:',
':icecream:', ':ice_cream:', ':shaved_ice:', ':birthday:', ':cake:', ':cookie:',
':chocolate_bar:', ':candy:', ':lollipop:', ':honey_pot:', ':apple:',
':green_apple:', ':tangerine:', ':lemon:', ':cherries:', ':grapes:',
':watermelon:', ':strawberry:', ':peach:', ':melon:', ':banana:', ':pear:',
':pineapple:', ':sweet_potato:', ':eggplant:', ':tomato:', ':corn:', ':poop:', )


class User(object):
    def __init__(self):
        self.name = fake.name()
        self.user_id = generate_monzo_id('cus')


class Account(object):
    def __init__(self, user, currency):
        self.account_id = generate_monzo_id('acc')
        self.description = '%s\'s %s' % (user.name, fake.word().title())
        self.created = fake.date_time_between(start_date='-1y', end_date='now')
        self.balance = random.randint(1000, 100000)
        self.spend_today = random.randint(100, 10000)

        if currency == 'random':
            self.currency = fake.currency_code()
        else:
            self.currency = currency


class Address(object):
    def __init__(self):
        self.address = '%s %s' % (fake.building_number(), fake.street_name())
        self.city = fake.city()
        self.country = fake.country_code()
        self.postcode = fake.zipcode()
        self.latitude = fake.latitude()
        self.longitude = fake.longitude()
        self.region = fake.state()


class MerchantGroup(object):
    def __init__(self):
        self.merchant_group_id = generate_monzo_id('grp')


class Merchant(object):
    def __init__(self, groups):
        self.merchant_id = generate_monzo_id('merch')
        self.merchant_group_id = random.choice(groups).merchant_group_id
        self.created = fake.date_time_between(start_date='-1y', end_date='now')
        self.logo = fake.image_url(width=42, height=42)
        self.address = Address()
        self.emoji = emoji.emojize(random.choice(EMOJI))
        self.category = random.choice(CATEGORIES)
        self.name = fake.company()

        if random.random() < 0.1:
            self.name += ' ' + fake.company_suffix()


class Transaction(object):
    def __init__(self, account, merchants):
        self.transaction_id = generate_monzo_id('tx')
        self.description = fake.sentence()
        self.currency = account.currency
        self.merchant = random.choice(merchants)
        self.metadata = {}
        self.account_balance = random.randint(1000, 100000)
        self.amount = random.randint(-10000, -100)
        self.created = fake.date_time_between(start_date='-1y', end_date='now')

        if random.random() < 0.9:
            self.settled = fake.date_time_between(
                start_date=self.created,
                end_date='now',
            )
        else:
            self.settled = None

        if random.random() < 0.95:
            self.is_load = True
            self.amount *= -1
        else:
            self.is_load = False

        if random.random() < 0.1:
            self.notes = fake.paragraph()
        else:
            self.notes = ""


def generate_token():
    return fake.sha1(raw_output=False)


def generate_monzo_id(kind):
    return '%s_%d%s' % (
        kind,
        fake.pyint(),
        fake.pystr(min_chars=20, max_chars=20),
    )
