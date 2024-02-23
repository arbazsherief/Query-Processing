import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(8, 6))
plt.bar(languages, popularity, color='skyblue')

plt.grid(axis='y', linestyle='--', linewidth=0.5)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')


plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
