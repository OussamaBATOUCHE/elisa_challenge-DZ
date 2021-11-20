from shapely.geometry import shape, Point


mp = {
"geometry" : {
    "type" : "MultiPolygon",
    "coordinates" : [
        [
            [
                [ 24.5658540028, 60.6349243169 ],
                [ 24.5658588896, 60.6349244059 ],
                [ 24.5658565409, 60.6349555448 ],
                [ 24.5658540028, 60.6349243169 ]
            ]
        ],
        [
            [
                [ 24.5658759376, 60.6351941942 ],
                [ 24.5663864924, 60.6352034835 ],
                [ 24.5663661982, 60.6354725924 ],
                [ 24.5658978727, 60.6354640715 ],
                [ 24.5658759376, 60.6351941942 ]
            ]
        ]
    ]
}

}

polygon = shape(mp['geometry'])