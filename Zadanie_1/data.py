import srednia_predkosc_biegu

distance_input = int(input("Ile metrów przebiegłeś? "))
time_input = float(input("W jakim czasie? (w minutach) "))

your_avg_speed = srednia_predkosc_biegu.avg_speed_of_run(distance_input, time_input)

print(f"Twój średni czas biegu to {your_avg_speed:.2f} metrów na minutę ")