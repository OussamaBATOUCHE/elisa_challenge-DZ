/*
 * Copyright 2019 Google LLC. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/* eslint-disable no-undef, @typescript-eslint/no-unused-vars, no-unused-vars */
import "./style.css";
// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

let map: google.maps.Map, heatmap: google.maps.visualization.HeatmapLayer;

function initMap(): void {
    map = new google.maps.Map(document.getElementById("map") as HTMLElement, {
        zoom: 11,
        center: {lat: 60.1699, lng: 24.9384},
        mapTypeId: "satellite",
    });

    map.addListener('click', (e) => {
        let lat = e.latLng.lat();
        let lng = e.latLng.lng();
        console.log(lat, lng);
    })

    /*document
        .getElementById('files')!
        .addEventListener('change', readSingleFile);
     */

    document.getElementById('monday')!
        .addEventListener('click', switchLayerToMonday)

    document.getElementById('tuesday')!
        .addEventListener('click', switchLayerToTuesday)

    document.getElementById('wednesday')!
        .addEventListener('click', switchLayerToWednesday)

    document.getElementById('thursday')!
        .addEventListener('click', switchLayerToThursday)

    document.getElementById('friday')!
        .addEventListener('click', switchLayerToFriday)

    document.getElementById('saturday')!
        .addEventListener('click', switchLayerToSaturday)

    document.getElementById('sunday')!
        .addEventListener('click', switchLayerToSunday)

    document.getElementById('5g')!
        .addEventListener('click', switchTo5G)

    document.getElementById('4g')!
        .addEventListener('click', switchTo4G)

    document.getElementById('5g_season')!
        .addEventListener('click', switchTo5gSeason)

    document.getElementById('summer')!
        .addEventListener('click', switchToSummer)

    document.getElementById('fall')!
        .addEventListener('click', switchToFall)

    fetchFile('get_4g_days');
}

function switchToSummer() {
    heatmap.set('data', summer)
}

function switchToFall() {
    heatmap.set('data', fall)
}

function switchLayerToMonday() {
    heatmap.set('data', monday)
}

function switchLayerToTuesday() {
    heatmap.set('data', tuesday)
}

function switchLayerToWednesday() {
    heatmap.set('data', wednesday)
}

function switchLayerToThursday() {
    heatmap.set('data', thursday)
}

function switchLayerToFriday() {
    heatmap.set('data', friday)
}

function switchLayerToSaturday() {
    heatmap.set('data', saturday)
}

function switchLayerToSunday() {
    heatmap.set('data', sunday)
}

function switchTo5G() {
    heatmap.set('map', null)
    fetchFile('get_5g_days')
}

function switchTo4G() {
    heatmap.set('map', null)
    fetchFile('get_4g_days')
}

function switchTo5gSeason() {
    heatmap.set('map', null)
    fetchSeasonFile()
}

const gradient = [
    "rgba(0, 255, 255, 0)",
    "rgba(0, 255, 255, 1)",
    "rgba(0, 191, 255, 1)",
    "rgba(0, 127, 255, 1)",
    "rgba(0, 63, 255, 1)",
    "rgba(0, 0, 255, 1)",
    "rgba(0, 0, 223, 1)",
    "rgba(0, 0, 191, 1)",
    "rgba(0, 0, 159, 1)",
    "rgba(0, 0, 127, 1)",
    "rgba(63, 0, 91, 1)",
    "rgba(127, 0, 63, 1)",
    "rgba(191, 0, 31, 1)",
    "rgba(255, 0, 0, 1)",
];

const monday: any[] = [];
const tuesday: any[] = [];
const wednesday: any[] = [];
const thursday: any[] = [];
const friday: any[] = [];
const saturday: any[] = [];
const sunday: any[] = [];

const API_URL = 'http://localhost:5000/'

function fetchFile(file) {
    fetch(API_URL + file)
        .then(response => {
           return response.body!
               .getReader()
               .read();
        }).then(data => {
        // @ts-ignore
        const blob = new Blob([data.value!.buffer], {type: 'text/plain; charset=utf-8'});
        return blob.text()
    }).then(text => {
        const dataArray = text.split('\n');
        dataArray.forEach((entry) => {
            const array = entry.split(",")
            let lng = +array[1];
            let lat = +array[2];
            let day = +array[3];
            let weight = +array[4];
            if (!isNaN(lat) && !isNaN(lng) && !isNaN(weight)) {
                let coordinate = {location: new google.maps.LatLng(lat, lng), weight: weight};
                switch (day) {
                    case 1 : {
                        monday.push(coordinate);
                        break;
                    }
                    case 2: {
                        tuesday.push(coordinate);
                        break;
                    }
                    case 3: {
                        wednesday.push(coordinate);
                        break;
                    }
                    case 4: {
                        thursday.push(coordinate);
                        break;
                    }
                    case 5: {
                        friday.push(coordinate);
                        break;
                    }
                    case 6: {
                        saturday.push(coordinate);
                        break;
                    }
                    case 7: {
                        sunday.push(coordinate);
                        break;
                    }
                }
            }

        })
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: monday,
            map: map,
            dissipating: true,
            opacity: 0.8,
        });
        heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
        heatmap.set("radius", heatmap.get("radius") ? null : 50);
    })
}

const summer :any[] = []
const fall :any[] = []

function fetchSeasonFile() {
    fetch(API_URL + 'get_5g_season')
        .then(response => {
            return response.body!
                .getReader()
                .read();
        }).then(data => {
        // @ts-ignore
        const blob = new Blob([data.value!.buffer], {type: 'text/plain; charset=utf-8'});
        return blob.text()
    }).then(text => {
        const dataArray = text.split('\n');
        dataArray.forEach((entry) => {
            const array = entry.split(",")
            let lng = +array[1];
            let lat = +array[2];
            let day = +array[3];
            let weight = +array[4];
            if (!isNaN(lat) && !isNaN(lng) && !isNaN(weight)) {
                let coordinate = {location: new google.maps.LatLng(lat, lng), weight: weight};
                switch (day) {
                    case 3 : {
                        summer.push(coordinate);
                        break;
                    }
                    case 4: {
                        fall.push(coordinate);
                        break;
                    }
                }
            }

        })
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: summer,
            map: map,
            dissipating: true,
            opacity: 0.8,
        });
        heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
        heatmap.set("radius", heatmap.get("radius") ? null : 50);
    })
}

/*function readSingleFile(e) {
    const file = e.target.files[0];
    if (!file) {
        return;
    }

    // @ts-ignore
    const reader = new FileReader();
    reader.onload = function (e) {
        const contents = e!.target!.result;
        const dataArray = (contents as string).split('\n');
        dataArray.forEach((entry) => {
            const array = entry.split(",")
            let lng = +array[1];
            let lat = +array[2];
            let day = +array[3];
            let weight = +array[4];
            if (!isNaN(lat) && !isNaN(lng) && !isNaN(weight)) {
                let coordinate = {location: new google.maps.LatLng(lat, lng), weight: weight};
                switch (day) {
                    case 1 : {
                        monday.push(coordinate);
                        break;
                    }
                    case 2: {
                        tuesday.push(coordinate);
                        break;
                    }
                    case 3: {
                        wednesday.push(coordinate);
                        break;
                    }
                    case 4: {
                        thursday.push(coordinate);
                        break;
                    }
                    case 5: {
                        friday.push(coordinate);
                        break;
                    }
                    case 6: {
                        saturday.push(coordinate);
                        break;
                    }
                    case 7: {
                        sunday.push(coordinate);
                        break;
                    }
                }
            }

        })
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: monday,
            map: map,
            dissipating: true,
            opacity: 0.8,
        });
        heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
        heatmap.set("radius", heatmap.get("radius") ? null : 50);
    };
    reader.readAsText(file);
}*/

export {initMap};

