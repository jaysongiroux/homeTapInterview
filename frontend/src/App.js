import { Component } from 'react';
import './App.css';
import ApiButton from './component/ApiButton';
import PropertyDetails from './component/PropertyDetails';
import ReactLoading from 'react-loading';

export default class App extends Component {
  constructor(){
    super();
    this.state = {
      propertyDetails: {},
      sewer: {},
      loading: false
    }

    this.determineSewer = this.determineSewer.bind(this);
    this.determinePropDetails = this.determinePropDetails.bind(this);
  }

  // When Button is pressed...
  determineSewer(e){
    e.preventDefault();
    this.setState({loading: true})
    fetch('http://localhost:105/hasSewer?add=123+Main+st&zip=02911')
    .then(resp => resp.json())
    .then(data => {
      this.setState({
        sewer: data,
        loading: false
      })
    })
    .catch(() => {
      alert("Sorry! Unable to fetch type of sewer")
      this.setState({
        loading: false
      })
    })
  }

  determinePropDetails(e){
    e.preventDefault();
    this.setState({loading: true})
    fetch('http://localhost:105/propertyDetails?add=123+Main+st&zip=02911')
    .then(resp => resp.json())
    .then(data => {
      this.setState({
        propertyDetails: data,
        loading: false
      })
    })
    .catch(() => {
      alert("Sorry! Unable to fetch property details")
      this.setState({
        loading: false
      })
    })
  }
  
  render(){
    return (
      <div className="App">
        {this.state.loading &&
          <div className="Loading">
            <ReactLoading className={'spinner'} type={'spin'} color={'blue'} height={200} width={100} />
          </div>
        }
        <h2>Home Tap Interview</h2>
        <div className={'buttonsContainer'}>
          <ApiButton text={"Display Type of sewer"}  determineSewer={this.determineSewer}/>
          <ApiButton text={"Display Property Details"}  determineSewer={this.determinePropDetails}/>
        </div>
        <div className="row">
          <PropertyDetails  title={'Sewer Details'} 
            text={this.state.sewer} clear={() => this.setState({sewer: {}})}/>
          <PropertyDetails  title={'Property Details'} 
            text={this.state.propertyDetails}  clear={() => {this.setState({propertyDetails: {}})}}/>
        </div>
      </div>
    );
  }
}
