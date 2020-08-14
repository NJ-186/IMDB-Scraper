from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class IMDBBot(object):
	"""docstring for TwitterBot"""
	def __init__(self):
		self.bot = webdriver.Firefox(executable_path = '/Users/dipali/opt/anaconda3/lib/python3.7/geckodriver')

	def imdb(self):
		bot = self.bot
		bot.get('https://www.imdb.com/chart/top/')
		time.sleep(2)

		containers = bot.find_elements_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr')
		container = [item.find_element_by_class_name('titleColumn') for item in containers]
		link_a = [contain.find_element(By.TAG_NAME, 'a') for contain in container]
		links = [link_tag.get_attribute('href') for link_tag in link_a]	

		newfile = 'imdb1.csv'

		f = open(newfile,'w')

		headers = 'Name,Rated,Running Length,Genre,Release Date,Director,IMDB-Rating \n'

		f.write(headers)

		i=0

		for link in links:
			bot.get(link)
			try:
				title = bot.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1').text
			except:
				title = ' '
			
			try:
				rating = bot.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span').text
			except:
				rating = ' '
			
			try:
				rate1 = bot.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div').text
			except:
				rate1 = ' '

			try:
				director = bot.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a').text
			except:
				director = ' '

			rate = rate1.replace(',','-')

			i+=1
			f.write(str(i) + ',' + title.replace(',','-') + ',' + rate.replace('|',',') + ',' + director + ',' + rating + '\n')

		f.close()

new_bot = IMDBBot()
new_bot.imdb()

