from mrjob.job import MRJob
from mrjob.step import MRStep

class covid19(MRJob):
    # Simple example + sort by amounts

    def steps(self):
         return [
            MRStep(
                mapper=self.mapper_get_cases,
                reducer=self.reducer_total_by_country_name),
            MRStep(
                mapper=self.mapper_make_amount_as_key,
                reducer=self.reducer_output),
        ]

    def mapper_get_cases(self,_, line):
        (date,daily_cases, daily_deaths, country) = line.split(',')
        yield country, int(daily_cases)

    def reducer_total_by_country_name(self, country, daily_cases):
        yield country, sum(daily_cases)   

    def mapper_make_amount_as_key(self, country, total_cases):
        yield '%01d' % int(total_cases), country

    def reducer_output(self, total_cases, country):
        for user in country:
            yield user, total_cases


if __name__ == '__main__':
    covid19.run()
