<template>
    <div>
        <v-spacer></v-spacer>
        <h4 class="text-h4 text-center " id="location-search">위치 검색</h4>
        <div id="map"></div> 

        <v-sheet max-width="100%" class="my-3">
        <v-form validate-on="submit lazy" @submit.prevent="searchBankLocation(where)" >
          <v-text-field
            v-model="where"
            class="bg-indigo-lighten-5"
            label="위치를 입력하세요"
          ></v-text-field>

          <v-btn
            :loading="loading"
            type="submit"
            block
            class="mt-2"
            text="Submit"
          ></v-btn>
        </v-form>
        </v-sheet>
        <v-spacer></v-spacer>

        <div class="button-group">
            <v-btn @click="searchonThisplace">현재 위치에서 다시 검색</v-btn>
            <v-btn @click="displayMarker([])">마커 지우기</v-btn>
            <v-btn @click="changeSize(800)">show</v-btn>
            <v-btn @click="changeSize(0)">hide</v-btn>
        </div>
    </div>
</template>

<script>
import { toRaw, ref, computed } from "vue";
import { useNavbarStore } from '@/stores/navbar';

export default {
    name: "KakaoMap",
    data() {
        return {
            markerPosition3: [
            ],
            markers: [],
            infowindow: null,
        };
    },
    mounted() {
        if (window.kakao && window.kakao.maps) {
            this.initMap();
        } else {
            const script = document.createElement("script");
            /* global kakao */
            script.onload = () => kakao.maps.load(this.initMap);
            script.src =
                "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=ed31ef236772d14e1f6cf3718d06e73d&libraries=services";
            // console.log(kakao)
            document.head.appendChild(script);
        }
        const navbar = useNavbarStore()
        const sidebar = ref([
            {
                id : 'locationSearch',
                name: '위치 검색'
            },
        ])
        navbar.navBarList.value = sidebar.value

    },
    methods: {
        initMap() {
            const container = document.getElementById("map");
            const options = {
                center: new kakao.maps.LatLng(33.450701, 126.570667),
                level: 5,
            };

            //지도 객체를 등록합니다.
            //지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
            this.map = new kakao.maps.Map(container, options);
            // 여기서 문제가 생기는구만
            const zoomControl = new kakao.maps.ZoomControl();
            this.map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
        },
        changeSize(size) {
            const container = document.getElementById("map");
            container.style.height = `${size}px`;
            toRaw(this.map).relayout();
        },
        displayMarker(markerPositions, names) {

            if (this.markers.length > 0) {
                this.markers.forEach((marker) => marker.setMap(null));
            }
            // console.log(markerPositions)
            // 이미 마커가 있으면 0으로 바꾼다는 것 같음
            const positions = markerPositions.map(
                (position) => new kakao.maps.LatLng(...position)
            );
            // MAP함수로 안에 있는 내용물들을 바꾼 함수를 가져오고
            // 그냥 위/경도를 이용하는게 아니라 LatLng를 통한 뭐로 바뀌어야함
            // console.log(positions)
            console.log(names)
            if (positions.length > 0) {
                this.markers = positions.map(
                    (position, index) =>
                        new kakao.maps.Marker({
                            map: toRaw(this.map),
                            position,
                            title: names[index],
                            clickable: true
                        })
                );

                this.markers.forEach(
                    (arg) => {
                        kakao.maps.event.addListener(arg, 'click', (event) => {
                            this.displayInfoWindow(arg.getPosition(), arg.getTitle())
                        })
                    }
                )

                const bounds = positions.reduce(
                    (bounds, latlng) => bounds.extend(latlng),
                    new kakao.maps.LatLngBounds()
                )

                console.log(bounds)
                toRaw(this.map).setBounds(bounds);


            }
        },

        // 내용 추가하는 기능까지 생성
        // 쿼리를 하는 내용은 없음 API기능에서는 REST로 하는걸로 보이는데 여기선 그냥 위치만 이동하네

        displayInfoWindow(position, name) {
            if (this.infowindow && this.infowindow.getMap()) {
                this.infowindow.close()
            }

            console.log(position, name, '입니다')
            var iwContent = `<div style="padding:5px; font-size :10px ">${name}</div>`, // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                // iwPosition = new kakao.maps.LatLng(position), //인포윈도우 표시 위치입니다
                iwPosition = position, //인포윈도우 표시 위치입니다
                iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

            this.infowindow = new kakao.maps.InfoWindow({
                map: toRaw(this.map), // 인포윈도우가 표시될 지도
                // 원시 객체를 준다는
                position: iwPosition,
                content: iwContent,
                removable: iwRemoveable,
            });

            // toRaw(this.map).setCenter(iwPosition);
        },

        searchBank() {
            const places = new kakao.maps.services.Places() 
            places.setMap(toRaw(this.map))
            const callback = (result, status) => {

                if (status === kakao.maps.services.Status.OK) {
                    console.log(result)
                    const positions = ref(result.map(
                        (position) => [Number(position.y), Number(position.x)]
                    ))
                    const names = ref(result.map(
                        (name) => name.place_name
                    ))
                    this.displayMarker(positions.value, names.value)
                }
            }

            const options = {
                location: toRaw(this.map).getCenter(),
                radius: 500,
                sort: map.DISTANCE,
                // useMapCenter : true,
            }

            places.keywordSearch('은행', callback, options)
        },
        searchonThisplace() {
            const places = new kakao.maps.services.Places()
            places.setMap(toRaw(this.map))
            const callback = (result, status) => {

                if (status === kakao.maps.services.Status.OK) {
                    console.log(result)
                    const positions = ref(result.map(
                        (position) => [Number(position.y), Number(position.x)]
                    ))
                    const names = ref(result.map(
                        (name) => name.place_name
                    ))
                    this.displayMarker(positions.value, names.value)
                }
            }

            const options = {
                // location: toRaw(this.map).getCenter(),
                useMapCenter: true,
                // bounds : toRaw(this.map).getBounds(),
                useMapBounds: true
                // useMapCenter : true,
            }

            places.keywordSearch('은행', callback, options)
        },
        searchBankLocation(where) {
            const places = new kakao.maps.services.Places()
            console.log(where)
            places.setMap(toRaw(this.map))


            const callback = (result, status) => {
                if (status === kakao.maps.services.Status.OK) {
                    const postition_obj = {}

                    const positions = ref(result.map(
                        (position) => [Number(position.y), Number(position.x)]
                    ))
                    const names = ref(result.map(
                        (name) => name.place_name
                    ))
                    this.displayMarker(positions.value, names.value)
                }
            }
            
            const callback2 = (result, status) => {
                if (status === kakao.maps.services.Status.OK) {
                    const postition_obj = {}
                    
                    const positions = ref(result.map(
                        (position) => [Number(position.y), Number(position.x)]
                    ))
                    console.log(positions.value[0][0], '=====================================')
                    const options = {
                        location: new kakao.maps.LatLng(positions.value[0][0], positions.value[0][1]),
                        radius: 4000,
                        sort: map.DISTANCE,
                        // useMapCenter : true,
                    }
                    places.keywordSearch('은행', callback, options)
                }
            }
            const options = {
                sort: map.DISTANCE,
                // useMapCenter : true,
            }
            places.keywordSearch(where, callback2, options)

            

        }
    },
};
const where = ref('')
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
    width: 100%;
    height: 400px;
}

.button-group {
    margin: 10px 0px;
}

button {
    margin: 0 3px;
}
</style>