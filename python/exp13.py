# Input probabilities
prob_rain = float(input("Enter P(Rain): "))
prob_traffic_given_rain = float(input("Enter P(Traffic | Rain): "))
prob_traffic = float(input("Enter P(Traffic): "))

# Bayes theorem
prob_rain_given_traffic = (prob_traffic_given_rain * prob_rain) / prob_traffic

# Output
print("P(Rain | Traffic) =", prob_rain_given_traffic)
