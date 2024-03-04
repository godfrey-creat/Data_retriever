class UserInterface:
    def __init__(self):
        self.database = Database()
        self.data_processor = DataProcessor()

    def run(self):
        query = input("Enter query: ")
        results = self.database.execute_query(query)
        processed_results = self.data_processor.process_data(results)
        self.display_results(processed_results)

    def display_results(self, results):
        # Display results to the user
        ...
