

class WeatherLocators(object):

    CLOUDCOVER = ["0", "0%-6%", "6%-19%", "19%-31%", "31%-44%", "44%-56%", 
                  "56%-69%", "69%-81%", "81%-94%", "94%-100%"] 
    SEEING = ["0", "<0.5", "0.5-0.75", "0.75-1", "1-1.25", "1.25-1.5", 
              "1.5-2", "2-2.5", ">2.5"]
    WINDSP = ["calm", "light", "moderate", "fresh", "strong", "gale", 
              "storm", "hurricane"]
              
    RH = ["0", "0%-5%", "5%-10%", "10%-15%", "15%-20%", "25%-30%", "35%-40%", "54%-50%",
          "50%-55%", "60%-65%", "65%-70%", "70%-75%", "75%-80%", "80%-85%", 
          "85%-90%", "90%-95%", "95%-99%", "100%"]
    