// Example of multipolygon:
const multiPolygon = [
    [
      [51.51, -0.12],
      [51.51, -0.13],
      [51.53, -0.13],
    ],
    [
      [51.51, -0.05],
      [51.51, -0.07],
      [51.53, -0.07],
    ],
  ]


{this.state.multipolygons.map((multiPolygon) => {
    return (
       <Polygon pathOptions={whateverOptions} positions={multiPolygon} />
    );
  })}