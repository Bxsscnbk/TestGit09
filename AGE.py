import pandas as pd

# Base data
data = {'Country': ['Thailand', 'India', 'Brazil'],
        'Name': ['John', 'Anna', 'James'],
        'Age': [28, 22, 30]}

# Standard DataFrame
df = pd.DataFrame(data)

# Extending DataFrame
class People(pd.DataFrame):
    @property
    def __constructor(self):
        return People

    # Encapsulated method
    def __age_in_decades(self):
        # Calculates the age in decades.
        return self['Age'] / 10

    def report_age_in_decades(self):
        return self.__age_in_decades()

    # Overriding a method to demonstrate polymorphism
    def sum(self):
        data_sum = super().sum()
        if 'Age' in data_sum:
            data_sum['Age'] = self.__age_in_decades().sum()  # Sum ages in decades
        return data_sum

# Polymorphism demonstration
print("DataFrame sum:")
print(df.sum())  # Sums each column in the DataFrame

print("\nPeople sum (polymorphic behavior):")
people_df = People(data)
print(people_df.sum())  # Uses overridden sum to behave differently for People

print(df.info(verbose=False))
