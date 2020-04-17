# Beatles Wordcloud (Datamining I)

This script creates a basic wordcloud using the link text from the ```<a>``` tags
on the [Beatles Wikipedia page](https://en.wikipedia.org/wiki/The_Beatles).

For an example, checkout [the image in this repo](./beatles-cloud.png).

## Dependencies

You will need Python 3 to run this program.

```shell script
pip3 install -r requirements.txt
```

## Running the Program

```shell script
# output file to desktop
./beatle-cloud.py -f ~/Desktop/cloud.png

# with additional stopwords
./beatle-cloud.py -f ~/Desktop/cloud.png -s "John" "Paul" "George" "Ringo"
```

*Note: "Beatle", "Beatles", "Album", "Albums", and "Band" are included as stopwords by default (in addition to traditional stop words)*
