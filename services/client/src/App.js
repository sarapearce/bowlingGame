import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import RunOptions from './sections/bowl';
import { Tab, TabButtonGroup, TabContent } from './components/tabs';



class App extends Component {
  constructor(props) {
    window.debug = () => {
      console.log(this.state);
    };
    super(props);
    this.state = {

    };
    //
    // this.changeTab = this.changeTab.bind(this);
    // this.changePressureTab = this.changeTab('pressure');
    // this.changeEquipmentTab = this.changeTab('equipment');
    // this.showReport = this.setter.bind(this, 'showReport');
    //
    // this.setPressure = this.setter.bind(this, 'pressure');
    // this.setRunDuration = this.setter.bind(this, 'runDuration');
    // this.setAutonomy = this.setter.bind(this, 'autonomy');
    // this.setBatterySize = this.setter.bind(this, 'batterySize');
    // this.setBatteryEfficiency = this.setter.bind(this, 'batteryEfficiency');
    // this.setSafetyFactor = this.setter.bind(this, 'safetyFactor');
    // this.setFlowRate = this.setter.bind(this, 'flowRate');
    // this.setPanel = this.setter.bind(this, 'panel');
    //
    // this.setPanels = this.setter.bind(this, 'panels');
    // this.setBatteries = this.setter.bind(this, 'batteries');
    //
    // this.setFilterMotor = this.setter.bind(this, 'filterMotor');
    // this.setFilterPlunger = this.setter.bind(this, 'filterPlunger');
    // this.setFilterHead = this.setter.bind(this, 'filterHead');
    // this.setFilterControl = this.setter.bind(this, 'filterControl');
    //
    // this.setLocation = this.setLocation.bind(this);
    // this.getSizingData = this.getSizingData.bind(this);
    // this.getFilteredSizing = this.getFilteredSizing.bind(this);
    // this.getEquipFilteredSizing = this.getEquipFilteredSizing.bind(this);
  }

  componentDidMount() {
    this.getData('locations');
  }

  getData(endpoint) {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}${endpoint}`)
      .then((res) => {
        if (endpoint !== 'locations') {
        this.setState({ [endpoint]: res.data.data.types });
      } else {
        this.setState({ [endpoint]: res.data.data.types }, () => {
          // organize and assign locations after we get location data in state
          this.sortLocations();
          this.setLocation(this.state.locations[0].Location);
        });
      }
      })
      .catch((err) => { console.log('Inside Appjs  ' + err); });
  }

  changeTab(name) {
    return e => {
      this.setState({
        tab: name,
      });
    };
  }

  setter(attr, input) {
    this.setState({[attr]: input });
  }

  render() {

    return (
      <div className="App">
        <Bowl {...this.state}/>{' '}
      </div>{' '}
    );
  }
}

export default App;
