from datetime import datetime


def get_month(month):
    match month:
        case 1:
            return 'Jan'
        case 2:
            return 'Feb'
        case 3:
            return 'Mar'
        case 4:
            return 'Apr'
        case 5:
            return 'May'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'Aug'
        case 9:
            return 'Sep'
        case 10:
            return 'Oct'
        case 11:
            return 'Nov'
        case 12:
            return 'Dec'

now = datetime.now()
print(now)
print(f'Today is{now.day , get_month(now.month) , now.year}')
