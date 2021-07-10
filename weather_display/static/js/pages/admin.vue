<template>
    <div class="admin">

        <h1>Station Admin</h1>
        <h2>Station List</h2>
        <b-table :items="stations" />
        <h2>Add New Station</h2>
        <b-form @submit="addStation" @reset="reset_form">
            <b-container>
                <b-row>
                    <b-col>

                        <b-form-group
                                label="Station name"
                                label-for="station-name-input"
                                description="Human readable name for weather station"
                        >
                            <b-form-input
                                    id="station-name-input"
                                    v-model="station_form.name"
                                    placeholder="Enter station name"
                                    required
                            ></b-form-input>
                        </b-form-group>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group
                                label="Rain Sensor"
                                label-for="station-rain-input"
                                description="Has a rain level sensor"
                        >
                            <b-form-checkbox
                                    id="station-rain-input"
                                    v-model="station_form.has_rain"
                                    required />

                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group
                                label="Light Sensor"
                                label-for="station-lux-input"
                                description="Has a light level sensor"
                        >
                            <b-form-checkbox
                                    id="station-lux-input"
                                    v-model="station_form.has_lux"
                                    required />

                        </b-form-group>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group
                                label="Temperature Sensor"
                                label-for="station-temp-input"
                                description="Has thermometer"
                        >
                            <b-form-checkbox
                                    id="station-temp-input"
                                    v-model="station_form.has_temp"
                                    required />

                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group
                                label="Pressure Sensor"
                                label-for="station-pressure-input"
                                description="Has a barometric pressure sensor"
                        >
                            <b-form-checkbox
                                    id="station-pressure-input"
                                    v-model="station_form.has_pressure"
                                    required />

                        </b-form-group>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group
                                label="Wind Speed Sensor"
                                label-for="station-wind-speed-input"
                                description="Has wind speed sensor"
                        >
                            <b-form-checkbox
                                    id="station-wind-speed-input"
                                    v-model="station_form.has_wind_speed"
                                    required />

                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group
                                label="Wind Direction Sensor"
                                label-for="station-wind-direction-input"
                                description="Has a wind direction sensor"
                        >
                            <b-form-checkbox
                                    id="station-wind-direction-input"
                                    v-model="station_form.has_wind_dir"
                                    required />

                        </b-form-group>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group
                                label="Humidity Sensor"
                                label-for="station-humidity-input"
                                description="Has humidity sensor"
                        >
                            <b-form-checkbox
                                    id="station-humidity-input"
                                    v-model="station_form.has_humidity"
                                    required />

                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-button type="submit" variant="primary">Submit</b-button>
                        <b-button type="reset" variant="danger">Reset</b-button>
                    </b-col>
                </b-row>
            </b-container>
        </b-form>
    </div>
</template>

<script>
    import Vuex from 'vuex';
    const axios = require("axios");
    import Vue from "vue/dist/vue.esm.js";
    import VueCookies from "vue-cookies";
    Vue.use(VueCookies);
    export default {
        name: "Admin",
        components: {
        },
        data(){
            return {
                station_form: {
                    'name': '',
                    'has_rain': false,
                    'has_temp': false,
                    'has_humidity': false,
                    'has_wind_speed': false,
                    'has_wind_dir': false,
                    'has_lux': false,
                    'has_pressure': false,
                }
            };
        },
        computed: {
            ...Vuex.mapState({
                stations: state => state.stations.stations
            })
        },
        watch: {
        },
        mounted() {
            this.getInitialData();
        },
        methods: {
            getInitialData(){
                this.$store.dispatch('stations/get_stations');
            },
            reset_form(){
                this.station_form.name = '';
                this.station_form.has_rain = false;
                this.station_form.has_temp = false;
                this.station_form.has_humidity = false;
                this.station_form.has_wind_speed = false;
                this.station_form.has_wind_dir = false;
                this.station_form.has_lux = false;
                this.station_form.has_pressure = false;
            },
            addStation(e){
                let vue = this;
                e.preventDefault();
                axios.post(
                    '/api/stations/',
                    this.station_form,
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': $cookies.get("csrftoken")
                        }
                    }
                ).then(function(response) {
                    vue.$store.dispatch('stations/add_station', response.data);
                    vue.reset_form();
                });
            }
        }
    };
</script>

<style lang="scss">
    .admin{
        background-color: #2aabd2;
    }
</style>
