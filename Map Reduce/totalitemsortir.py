from mrjob.job import MRJob
from mrjob.step import MRStep

class totalitemsortir(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_itemID,
                   reducer=self.reducer_totals_by_customer),
            MRStep(mapper=self.mapper_make_amounts_key,
                   reducer=self.reducer_output_results)
        ]
    def mapper_get_itemID(self, _, line):
        (customerID, itemID, orderAmount) = line.split(',')
        yield customerID, float(itemID)

    def reducer_totals_by_customer(self, customerID, itemID):
        yield customerID, sum(itemID)

    def mapper_make_amounts_key(self, customerID, itemTotal):
        yield '%04.02f'%float(itemTotal), customerID
        
    def reducer_output_results(self, itemTotal, customerIDs):
        for customerID in customerIDs:
            yield customerID, itemTotal

if __name__ == '__main__':
    totalitemsortir.run()
    