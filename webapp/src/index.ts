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
    zoom: 13,
    center: { lat: 60.1699, lng: 24.9384 },
    mapTypeId: "satellite",
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
  });

  document
    .getElementById("toggle-heatmap")!
    .addEventListener("click", toggleHeatmap);
  document
    .getElementById("change-gradient")!
    .addEventListener("click", changeGradient);
  document
    .getElementById("change-opacity")!
    .addEventListener("click", changeOpacity);
  document
    .getElementById("change-radius")!
    .addEventListener("click", changeRadius);
}

function toggleHeatmap(): void {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient(): void {
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

  heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
}

function changeRadius(): void {
  heatmap.set("radius", heatmap.get("radius") ? null : 20);
}

function changeOpacity(): void {
  heatmap.set("opacity", heatmap.get("opacity") ? null : 0.2);
}

// Heatmap data: 500 Points
function getPoints() {
  return [
    {location: new google.maps.LatLng(60.1699, 24.9384),  weight: 0.5},
    {location: new google.maps.LatLng(60.1700, 24.9384),  weight: 1},
    {location: new google.maps.LatLng(60.1701, 24.9384),  weight: 2},
    {location: new google.maps.LatLng(60.1702, 24.9384),  weight: 10},
    {location: new google.maps.LatLng(60.1703, 24.9384),  weight: 3},
    {location: new google.maps.LatLng(60.1704, 24.9384),  weight: 3.5},
    {location: new google.maps.LatLng(60.1705, 24.9384),  weight: 4.5},
    {location: new google.maps.LatLng(60.1706, 24.9384),  weight: 5.5},
    {location: new google.maps.LatLng(60.1707, 24.9384),  weight: 6.5},
  ];
}
export { initMap };
