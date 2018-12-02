
import { batteriesRequired, panelsRequired, panelsDailyOutput, flowPerDay } from '../calc';

test('batteriesRequired', function() {
  let autonomy = 2;
  let flowRate = 40;
  let batterySize = 100;
  let batteryEfficiency = 80.0;
  let safetyFactor = 1.2;
  let runDuration = 24;
  let slope = 0.09;
  let intercept = 0.06;

  let batteries = batteriesRequired({
    autonomy,
    flowRate,
    batterySize,
    batteryEfficiency,
    safetyFactor,
    runDuration,
    slope,
    intercept,
  });

  expect(batteries).toBeCloseTo(2.63519, 4);

  autonomy = 1;
  batteries = batteriesRequired({
    autonomy,
    flowRate,
    batterySize,
    batteryEfficiency,
    safetyFactor,
    runDuration,
    slope,
    intercept,
  });

  expect(batteries).toBeCloseTo(1.31759, 4);

  autonomy = 2;
  runDuration = 12;
  batteries = batteriesRequired({
    autonomy,
    flowRate,
    batterySize,
    batteryEfficiency,
    safetyFactor,
    runDuration,
    slope,
    intercept,
  });
  expect(batteries).toBeCloseTo(1.31759, 4);

  autonomy = 2;
  runDuration = 24;
  batteryEfficiency = 40;
  batteries = batteriesRequired({
    autonomy,
    flowRate,
    batterySize,
    batteryEfficiency,
    safetyFactor,
    runDuration,
    slope,
    intercept,
  });
  expect(batteries).toBeCloseTo(5.270399, 4);
});

test('panelsRequired', function() {
  let flowRate = 40;
  let safetyFactor = 1.2;
  let runDuration = 24;
  let slope = 0.09;
  let intercept = 0.06;
  let location = {
    State: 'Tx',
    City: 'Kenedy',
    'Sunlight, Min': '3.83',
    'Sunlight, Avg': '5.00',
    Location: 'Tx - Kenedy',
    Latitude: '28.81',
    Longitude: '-97.84',
    Declination: '4',
    'Tilt Angle': '25.00',
    'Declination Direction': '1',
  };
  let sunlightType = 'Sunlight, Min';
  let panelType = '60';

  let batteries = panelsRequired({
    flowRate,
    safetyFactor,
    runDuration,
    sunlightType, // Min or Average
    panelType, // Type of Panel 60W
    location, // Location object { }
    slope,
    intercept,
  });
  expect(batteries).toBeCloseTo(9.1738903, 4);

  sunlightType = 'Sunlight, Avg';

  batteries = panelsRequired({
    flowRate,
    safetyFactor,
    runDuration,
    sunlightType, // Min or Average
    panelType, // Type of Panel 60W
    location, // Location object { }
    slope,
    intercept,
  });
  expect(batteries).toBeCloseTo(7.0271, 3);

  runDuration = 12;

  batteries = panelsRequired({
    flowRate,
    safetyFactor,
    runDuration,
    sunlightType, // Min or Average
    panelType, // Type of Panel 60W
    location, // Location object { }
    slope,
    intercept,
  });
  expect(batteries).toBeCloseTo(3.5135, 3);
});

// Test the Flow Per Day function. This leads to the Max Flow Rate.
test('flowPerDay', function() {
  let numberOfBatteries = 2;
  let flowRate = 40;
  let batteryEfficiency = 0.8;
  let batterySize = 100;
  let safetyFactor = 1.2;
  let runDuration = 24;
  let slope = 0.09;
  let intercept = 0.06;
  let maxFlowRate = 12;

  let rate = flowPerDay({
    numberOfBatteries, // # of batteries
    batterySize, // Battery in Amp Hours
    batteryEfficiency, // 0-100 used to derate battery
    safetyFactor, // autonomy safety factor used to derate battery
    runDuration, // number of hours to run a day (default is 24)
    slope, // data from pump to calculate load based on flow
    intercept, // data from pump to calulate load based on flow
    maxFlowRate, // data from pump max flow rate
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(rate).toBeCloseTo(0, 4);

  batterySize = 150

  rate = flowPerDay({
    numberOfBatteries, // # of batteries
    batterySize, // Battery in Amp Hours
    batteryEfficiency, // 0-100 used to derate battery
    safetyFactor, // autonomy safety factor used to derate battery
    runDuration, // number of hours to run a day (default is 24)
    slope, // data from pump to calculate load based on flow
    intercept, // data from pump to calulate load based on flow
    maxFlowRate, // data from pump max flow rate
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(rate).toBeCloseTo(0, 4);

  numberOfBatteries = 3

  rate = flowPerDay({
    numberOfBatteries, // # of batteries
    batterySize, // Battery in Amp Hours
    batteryEfficiency, // 0-100 used to derate battery
    safetyFactor, // autonomy safety factor used to derate battery
    runDuration, // number of hours to run a day (default is 24)
    slope, // data from pump to calculate load based on flow
    intercept, // data from pump to calulate load based on flow
    maxFlowRate, // data from pump max flow rate
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(rate).toBeCloseTo(0, 4);

  runDuration = 12;

  rate = flowPerDay({
    numberOfBatteries, // # of batteries
    batterySize, // Battery in Amp Hours
    batteryEfficiency, // 0-100 used to derate battery
    safetyFactor, // autonomy safety factor used to derate battery
    runDuration, // number of hours to run a day (default is 24)
    slope, // data from pump to calculate load based on flow
    intercept, // data from pump to calulate load based on flow
    maxFlowRate, // data from pump max flow rate
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(rate).toBeCloseTo(0, 4);
});


// Test the panelsDailyOutput function.
test('panelsDailyOutput', function() {
  let numberOfPanels = 2; // number of panels
  let panelType = 60; // Type of Panel 60W
  let location = {
    State: 'Tx',
    City: 'Kenedy',
    'Sunlight, Min': '3.83',
    'Sunlight, Avg': '5.00',
    Location: 'Tx - Kenedy',
    Latitude: '28.81',
    Longitude: '-97.84',
    Declination: '4',
    'Tilt Angle': '25.00',
    'Declination Direction': '1',
  };// Location object { }
  let sunlightType = 'Sunlight, Min'; // Min or Average
  let safetyFactor = 1.2; // autonomy safety factor used to derate battery

  let numberOfBatteries = 2;
  let flowRate = 40;
  let batteryEfficiency = 0.8;
  let batterySize = 100;

  let runDuration = 24;
  let slope = 0.09;
  let intercept = 0.06;
  let maxFlowRate = 12;

  let output = panelsDailyOutput({
    numberOfPanels, // number of panels
    panelType, // Type of Panel 60W
    location, // Location object { }
    sunlightType, // Min or Average
    safetyFactor, // autonomy safety factor used to derate battery
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(output).toBeCloseTo(0, 4);

  batterySize = 150;

  output = panelsDailyOutput({
    numberOfPanels, // number of panels
    panelType, // Type of Panel 60W
    location, // Location object { }
    sunlightType, // Min or Average
    safetyFactor, // autonomy safety factor used to derate battery
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(output).toBeCloseTo(0, 4);

  numberOfBatteries = 3

  output = panelsDailyOutput({
    numberOfPanels, // number of panels
    panelType, // Type of Panel 60W
    location, // Location object { }
    sunlightType, // Min or Average
    safetyFactor, // autonomy safety factor used to derate battery
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(output).toBeCloseTo(0, 4);

  runDuration = 12;

  output = panelsDailyOutput({
    numberOfPanels, // number of panels
    panelType, // Type of Panel 60W
    location, // Location object { }
    sunlightType, // Min or Average
    safetyFactor, // autonomy safety factor used to derate battery
  });

  //Not these numbers. Need to get actual value from MS Access
  expect(output).toBeCloseTo(0, 4);
});
