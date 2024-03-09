from faker import Faker
faker_obj = Faker()
generated_sentences = [faker_obj.sentence() for _ in range(50)]

with open("lines.txt", "w") as file:
    for sentence in generated_sentences:
        file.write(sentence + '\n')