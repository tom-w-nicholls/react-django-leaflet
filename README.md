# react-django-leaflet
<h1> A Quick Demonstration of a simple Django/React/Leaflet project running in Docker</h1>

This demonstration application uses Django to serve GeoJson data via a REST API and react-leaflet to display it.

This can be all be run within a Docker container which utilises hot reload for development purposes.

Run locally using the commands:

```
docker-compose build
docker-compose up -d
```

Then go to http://localhost to view the results

The polygon data that this is based on is from a project completed in conjuction with Cumbria Action for Sustainability
to locate roof spaces in Penrith, Cumbria, UK that are judged using an algorithm to be most suitable for solar panels (using 3D elevation data).

To view: click on a roof space to view estimated potential solar energy generation per annum
