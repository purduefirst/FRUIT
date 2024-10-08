from PIL import Image, ImageDraw, ImageFont # thumbnails

translateSymbol = {'M': 'Playoffs', 'Q': 'Quals', 'F': 'Finals'}

# Define fonts and sizes used in the thumbnail
fontTeamNumbers = ImageFont.truetype('arialbd.ttf', 80)
fontMatchNumbers = ImageFont.truetype('arial.ttf', 300)
fontExtraInfo = ImageFont.truetype('arial.ttf', 100)

# Import logo of program (typ FRC)
logoProgram = Image.open('./FIRSTRobotics_IconVert_RGB.png', 'r').convert("RGBA")

# Define how team numbers are layed out
boxShape = (100, 300)   # height, width of boxes (px)
boxSpace = (50, 100)    # hspace, wspace between boxes (px)

def generateThumbnail(matchID:str, matchInfo:dict, eventDetails: str=None, sponsorPath: str=None, name: str=None):
    """Creates a 1920x1080px thumbnail image for YouTube match video

    Args:
        matchID (str): a combination of match type and number (Q23 = Quals 23, M5 = Playoffs 5, F1 = Finals 1)
        matchInfo (dict): data about the match
        eventDetails (str): building name \\n city \\n date
        sponsorPath (str): filepath to sponsor image (.jpg or .png)
        name (str): file name override, use None to follow naming convention 

    Returns:
        filePath (str): filepath to thumbnail png

    """

    # Create blank thumbnail
    thumbnail = Image.new("RGBA", (1920, 1080), "white")

    # Add in program and sponsor logo
    thumbnail.alpha_composite(logoProgram, (125,75//2))
    if sponsorPath != None:
        logoSponsorRaw = Image.open(sponsorPath, 'r').convert("RGBA")

        widthSponsor, heightSponsor = logoSponsorRaw.size
        logoScale = min([(1920*0.5*0.8)/widthSponsor, (1080*0.5*0.8)/heightSponsor])

        logoSponsor = logoSponsorRaw.resize((int(widthSponsor*logoScale),int(heightSponsor*logoScale)))

        widthSponsor, heightSponsor = logoSponsor.size
        thumbnail.alpha_composite(logoSponsor, (int(1920*3/4)-(widthSponsor//2),int(1080*3/4)-(heightSponsor//2)))

    # Prepare thumbnail to be drawn on
    draw = ImageDraw.Draw(thumbnail)

    # Add event location + dates
    if eventDetails != None:
        draw.multiline_text((int(1920*3/4), int(1080*3/4)), eventDetails, font=fontExtraInfo, fill='black', anchor="mm", align="center")

    # Draw alliance boxes and names
    for color, offset, teamNumbers in [('#ED1C24', 0, matchInfo['teamsRed']), ('#0066B3', boxSpace[1]+boxShape[1], matchInfo['teamsBlue'])]:
        for i, team in enumerate(teamNumbers):
            draw.rounded_rectangle((1080+offset, 75+(boxShape[0]+boxSpace[0])*i, 1080+boxShape[1]+offset, 75+boxShape[0]+(boxShape[0]+boxSpace[0])*i), fill=color, radius=15)
            draw.text((1080+offset+(boxShape[1]//2), 75+(boxShape[0]+boxSpace[0])*i+(boxShape[0]//2)), str(team), font=fontTeamNumbers, fill='white', anchor="mm")

    # Draw match label + number
    matchStyle = (str(translateSymbol[matchID[0]]).upper(), str(matchID[1:]))
    draw.text((int(1920*1/4), int(1080*3/4)-100), matchStyle[0], font=fontTeamNumbers, fill='black', anchor="md")
    draw.text((int(1920*1/4), int(1080*3/4)-100), matchStyle[1], font=fontMatchNumbers, fill='black', anchor="mt")

    # Save thumbnail to file
    if name == None:
        filePath = './output/thumbnails/'+matchStyle[0]+matchStyle[1]+'.png'
    else:
        filePath = name+'.png'
    
    thumbnail.save(filePath)
    return filePath