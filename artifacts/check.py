import pickle


print("response.pkl")
with open("response.pkl", "rb") as f:
    print(pickle.load(f))


print("#################################")
print("message.pkl")
with open("message.pkl", "rb") as f:
    print(pickle.load(f))


print("#################################")
print("usage.pkl")
with open("usage.pkl", "rb") as f:
    print(pickle.load(f))
