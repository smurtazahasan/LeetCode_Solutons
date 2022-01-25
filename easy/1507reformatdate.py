class Solution:

    # Runtime: 32ms
    # Space: 14.4MB
    def reformatDate(date):
        date = date.split()
        ## ['1st', 'Jan', '2022']
        
        ## Year ##
        year = date[2]
        
        ## Month ##
        monthDict={'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        month = monthDict[date[1]] if len(monthDict[date[1]]) != 1 else '0' + monthDict[date[1]]
        
        ## Day ##
        day = date[0][:-2] if len(date[0][:-2]) > 1 else '0' + date[0][:-2]
        
        return year + '-' + month + '-' + day


    # Runtime: 54ms
    # Space: 14.3MB
    def reformatDateFormat(date):
        day, month, year = date.split()
        if len(day) == 3: day = '0' + day
        monthDict={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        return "{}-{}-{}".format(year, monthDict[month], day[:-2])
