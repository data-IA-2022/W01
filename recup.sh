for fn in title.basics title.crew name.basics title.akas title.episode title.principals title.ratings
do
  echo "Récup $fn"
  wget https://datasets.imdbws.com/${fn}.tsv.gz -o data/${fn}.tsv.gz
done