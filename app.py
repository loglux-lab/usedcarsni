import cars

search_url = "https://www.usedcarsni.com/search_results.php?search_type=1&make=24&fuel_type=2&age_from=2016&price_from=0&user_type=2%7C4&model=1170&trans_type=0&age_to=0&price_to=0&mileage_to=0&keywords=&distance_enabled=1&distance_postcode=&body_style=12&doors%5B%5D=5"

all_renault2016 = "https://www.usedcarsni.com/search_results.php?keywords=&make=24&model=1170&fuel_type=0&trans_type=0&age_from=2016&age_to=0&price_from=0&price_to=0&user_type=0&mileage_to=0&body_style=12&doors%5B%5D=5&keywords=&distance_enabled=0&distance_postcode=&homepage_search_attr=1&tab_id=0&search_type=1"

convertable = "https://www.usedcarsni.com/search_results.php?keywords=&make=0&fuel_type=0&trans_type=0&age_from=0&age_to=0&price_from=0&price_to=0&user_type=0&mileage_to=0&body_style=5&keywords=&distance_enabled=0&distance_postcode=&homepage_search_attr=1&tab_id=0&search_type=1"

convertable_smalleng = "https://www.usedcarsni.com/search_results.php?search_type=1&make=0&fuel_type=1&age_from=0&price_from=0&user_type=0&trans_type=0&age_to=0&price_to=0&mileage_to=0&keywords=&distance_enabled=1&distance_postcode=&body_style=5&eng_size%5B%5D=999&eng_size%5B%5D=1000&eng_size%5B%5D=1200&eng_size%5B%5D=1300&eng_size%5B%5D=1400&eng_size%5B%5D=1500&eng_size%5B%5D=1600"

motor = cars.Cars(all_renault2016)
motor.start()
motor.results()
motor.save_to_excel()
motor.pd_table()
motor.save_to_db()



