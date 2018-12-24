# N2YO Python API

This python package is a wrapper to access the N2YO REST API.

For each transaction, the caller must be identified and authorized by a license key (API key). To generate a unique license key, users are requested first to register an account at n2yo.com. After login, please visit the profile page and scroll down to access the button that generates the API key. The new API key will be accessible in the profile and cannot be changed. If you need a new key, please contact us and provide an explanation. The keys issued for the SOAP Web Services API are not valid for REST API. 

The following functions are currently available: 

get_TLE: 
Retrieve the Two Line Elements (TLE) for a satellite identified by NORAD id. 

get_positions: Retrieve the future positions of any satellite as footprints (latitude, longitude) to display orbits on maps. Also return the satellite's azimuth and elevation with respect to the observer location. Each element in the response array is one second of calculation. First element is calculated for current UTC time. 

get_visualpasses: Get predicted visual passes for any satellite relative to a location on Earth. A "visual pass" is a pass that should be optically visible on the entire (or partial) duration of crossing the sky. For that to happen, the satellite must be above the horizon, illumintaed by Sun (not in Earth shadow), and the sky dark enough to allow visual satellite observation.
 
get_radiopasses: The "radio passes" are similar to "visual passes", the only difference being the requirement for the objects to be optically visible for observers. This function is useful mainly for predicting satellite passes to be used for radio communications. The quality of the pass depends essentially on the highest elevation value during the pass, which is one of the input parameters. 

get_above: The "above" function will return all objects within a given search radius above observer's location. The radius (θ), expressed in degrees, is measured relative to the point in the sky directly above an observer (azimuth). 