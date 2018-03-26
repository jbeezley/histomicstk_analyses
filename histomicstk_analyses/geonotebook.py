def convert_annotation(annotation, region):
    if annotation.get('type') != 'polyline':
        raise Exception('Unsupport annotation type')

    llx, lly, urx, ury = region.bounds
    w = urx - llx
    h = ury - lly
    coordinates = [
        [pt[0] * w + llx, pt[1] * h + lly]
        for pt in annotation['points']
    ]
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Polygon',
            'coordinates': [coordinates]
        },
        'properties': {
            'fillColor': annotation.get('fillColor', 'rgba(0,0,0,0)'),
            'lineColor': annotation.get('lineColor', 'rgb(0,255,0)')
        }
    }


def convert_annotations(annotations, region):
    return {
        'type': 'FeatureCollection',
        'features': [
            convert_annotation(annotation, region)
            for annotation in annotations
        ]
    }
