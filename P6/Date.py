class Date:
    #Constructor
    def __init__(self,month,day,year):
        self._month = month
        self._day = day
        self._year = year
    def leap_year(self):
        return ((self._year == 0) and not (self._year%100 == 0  and self._year%400 != 0))

    # Return the Date object one day after self
    def tomorrow(self):
        if self._month == 12 and self._day == 31:
            year = self._year + 1
            month = 1
            day = 1

            return(Date(month,day,year))
        
        elif self.leap_year() and self._month == 2 and self._day == 29:
            year = self._year + 1
            month = 3
            day = 1

            return(Date(month,day,year))

        elif self._month == 2 and self._day == 28:
            year = self._year + 1
            month = 3
            day = 1

            return(Date(month,day,year))

        elif self._month == 4 | 6 | 9 | 11 and self._day == 30:
            year = self._year
            month = self._month + 1
            day = 1

            return(Date(month,day,year))
        
        elif self._month == 1 | 3 | 5 | 7 | 8 | 10 and self._day == 31:
            year = self._year
            month = self._month + 1
            day = 1

            return(Date(month,day,year))

        else: 
            year = self._year
            month = self._month
            day = self._day + 1

            return(Date(month,day,year))

    # Returns the Date object obtained by adding ndays to self
    def add(self,ndays):
        day = self
        for item in range(ndays):
            day = day.tomorrow()
        return day

    # Returns True if self is before day
    def after(self,day):
        if self._year > day._year:
            return True
        elif self._year == day._year and self._month > day._month:
            return True
        elif self._year == day._year and self._month == day._month and self._day > day._day:
            return True
        else:
            return False

    # Returns True if self is same as day
    def equals(self,day):

        if self._year == day._year and self._month == day._month and self._day == day._day:
            return True
        return False

    # Returns True if self is after day
    def before(self,day):
        if self.after(day) == False and self.equals(day) == False:
            return True
        return False

    # Returns the number of days between self and day
    def no_of_days(self,month):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            return 31
        elif(month==2):
            if(self.leap_year()==True):
                return 29
            else:
                return 28
        else:
            return 30

    def days_between(self,d):
        if(self._month==d._month and self._year==d._year):
            return abs(self._day-d._day)
        else:
            current_days=self._day
            for i in range(1,self._month+1):
                current_days=current_days+self.no_of_days(i)
            d_days=d._day
            for i in range(1,d._month+1):
                d_days=d_days+d.no_of_days(i)
            return abs(current_days-d_days)
    '''def days_between(self,day):
        count = 0
        updated_day = self
        while True:
            if self.after(day) == True:
                day = day.tomorrow()
                count += 1
                if self.equals(day) == True:
                    break
            elif self.before(day) == True:
                updated_day = updated_day.tomorrow()
                count += 1
                if day.equals(updated_day) == True:
                    break 
            else:
                break
        return abs(count)'''
        
            
    def __str__(self):
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        return "{} {}, {}".format(str(self._day),str(months[self._month - 1]), self._year)


'''d1 = Date(12,12,2002)
d2 = Date(1,3,2012)

print(d1)
print(d1.tomorrow())
print(d1.add(10))
print(d1.add(20))                     # Edge Case
print(d1.after(Date(1,3,2012)))
print(d1.equals(Date(1,3,2012)))
print(d1.before(Date(1,3,2012)))
print(d1.days_between(Date(1,3,2012)))'''

