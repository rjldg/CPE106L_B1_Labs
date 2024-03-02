from faker import Faker

faker = Faker()

sentences = [faker.sentence() for _ in range(50)]   # prints 50 randomly generated sentences

with open("essay.txt", "w") as file:
    for sentence in sentences:
        file.write(sentence + '\n')