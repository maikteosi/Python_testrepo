from Address import Address
from Mailing import Mailing

to_address = Address("665000", "Иркутск", "Ленина", "11А", "2")
from_address = Address("665004", "Ангарск", "Ленина", "2/2", "7")


mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1000,
    track="RA123458989RU"
)


from_info = (f"{mailing.from_address.index}, {mailing.from_address.city}, "
             f"{mailing.from_address.street}, {mailing.from_address.home} - "
             f"{mailing.from_address.apartment}")

to_info = (f"{mailing.to_address.index}, {mailing.to_address.city}, "
           f"{mailing.to_address.street}, {mailing.to_address.home} - "
           f"{mailing.to_address.apartment}")

print(f"Отправление {mailing.track} из {from_info} в {to_info}. "
      f"Стоимость {mailing.cost} рублей.")
