
#for a given sentence we slip it into a dictionary with its word and it's length as it's value


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result={word:len(word) for word in sentence.split()}
print(result)
