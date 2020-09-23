/**
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

!function(){function a(a){window.addEventListener?window.addEventListener("load",a,!1):window.attachEvent&&window.attachEvent("onload",a)}function b(a){window.___gcfg={lang:a.lang,parsetags:a.parsetags}}function c(a,b){for(var c=[],d=0;d<a.length;d++){var e=a[d];b(e)&&c.push(e)}return c}function d(){return c(document.getElementsByTagName("script"),function(a){return a.src==w})}function e(a){return{hangout_type:a.getAttribute("hangout_type")||o,publisher_id:a.getAttribute("publisher_id")||r,render:a.getAttribute("render")||s,room_id:a.getAttribute("room_id")||h(),topic:a.getAttribute("topic")||t,widget_size:a.getAttribute("widget_size")||u,width:a.getAttribute("width")||v}}function f(a){return{lang:a[0].getAttribute("lang")||p,parsetags:a[0].getAttribute("parsetags")||q}}function g(a){return x+"-target-"+a}function h(){return"room_"+(window.location.href||"/")}function i(a,b){var c=d();c.length>=1&&k(w+" script already loaded; did you accidentally include it twice?");var e=document.createElement("script");e.async=!0,e.onload=b,e.type="text/javascript",e.src=w;var f=document.getElementsByTagName("script")[0];f.parentNode.insertBefore(e,f)}function j(a){for(var b=0;b<a.length;b++){var c=a[b],d=g(b);if(document.getElementById(d))return;var e=document.createElement("div");e.id=d,c.appendChild(e)}}function k(a){console&&console.log&&console.log(a)}function l(){var a=document.getElementsByClassName(x);if(0==a.length)return void k("No div elements of class "+x+" found");var b=f(a);n(b,m(a))}function m(a){return function(){for(var b=0;b<a.length;b++){var c=e(a[b]);gapi.hangout.render(g(b),{hangout_type:c.hangout_type,publisher_id:c.publisher_id,render:c.render,room_id:c.room_id,topic:c.topic,widget_size:c.widget_size,width:c.width})}}}function n(a,c){var d=document.getElementsByClassName(x);b(a),j(d),i(a,c)}var o="normal",p="en",q="explicit",r="112744459749475398119",s="hangout",t="Instant Hangout",u="136",v="300",w="https://apis.google.com/js/plusone.js",x="instanthangouts";a(l)}();
