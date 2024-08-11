from prac_09.silver_service_taxi import SilverServiceTaxi

EXPECTED_FARE = 48.78

silver_service_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2.0)
silver_service_taxi.drive(18)
fare = silver_service_taxi.get_fare()
assert fare == EXPECTED_FARE  # text the fare
print(fare)



