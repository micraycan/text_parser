from bs4 import BeautifulSoup

soup_first = BeautifulSoup(open("C://group[1].html", encoding = "utf8"), "html.parser")
soup_second = BeautifulSoup(open("C://group[2].html", encoding = "utf8"), "html.parser")
soup_third = BeautifulSoup(open("C://group[3].html", encoding = "utf8"), "html.parser")

first_group = soup_first.find_all('li')
second_group = soup_second.find_all('li')
third_group = soup_third.find_all('li')

name_list = []
sender_count = {}

def count_names(messages):
    # list to contain name for message sender
    for ol in messages:
        for sender in ol.find_all('li', {'class' : 'user-name'}):
            # get rid of the new line code
            name_list.append(sender.get_text()[1:-1])


count_names(first_group)
count_names(second_group)
count_names(third_group)

total_num = len(name_list)

# run through each name in list and count number of messages from that sender
for name in name_list:
    if name in sender_count:
        sender_count[name] += 1
    else:
        sender_count[name] = 1

# sorting in descending order (most to least messages sent)
ordered_count = sorted(sender_count, key = sender_count.__getitem__, reverse = True)

for sender in range(len(ordered_count)):
    print("{0}: {1} messages out of {2}: {3:.0f}%".format(ordered_count[sender],
          sender_count[ordered_count[sender]], total_num,
          sender_count[ordered_count[sender]]/total_num * 100))
