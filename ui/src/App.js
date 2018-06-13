import React, {Component} from 'react';
import axios from 'axios';

import logo from './Dr_Logo.png';
import './App.css';
import './css/multi-toggle.css'
import SymptomsSummary from "./components/left/symptoms-summary";
import SearchArea from "./components/middle/symptoms-search";
import DiseasePredictor from "./components/right/disease-predictor";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            symptoms: [],
            positiveSymptoms: [],
            negativeSymptoms: [],
            diseases: [],
            message: ""
        }
    }

    componentDidMount() {
        this.predictDisease(this.constructPayload());
        this.loadSymptoms();
    };

    predictDisease(payload) {
        axios.post('http://localhost:5000/diseases/predict', payload, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => this.setState({
                diseases: response.data
            }))
    };

    predictSymptoms(payload) {
        axios.post('http://localhost:5000/symptoms/predict', payload, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => this.setState({
                symptoms: response.data
            }))
    };

    loadSymptoms(payload) {
        axios.get('http://localhost:5000/symptoms', {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => this.setState({
                symptoms: response.data
            }))
    };

    constructPayload() {
        return ({
            positives: this.state.positiveSymptoms,
            negatives: this.state.negativeSymptoms
        });
    };

    submitFilters = (newPos, newNeg) => {
        this.state.positiveSymptoms = this.state.positiveSymptoms.concat(newPos);
        this.state.negativeSymptoms = this.state.negativeSymptoms.concat(newNeg);
        this.setState({positiveSymptoms: this.state.positiveSymptoms, negativeSymptoms: this.state.negativeSymptoms});
        this.predictDisease(this.constructPayload());
        this.predictSymptoms(this.constructPayload());
    };

    saveDiagnosis = (disease) => {
        axios.post('http://localhost:5000/symptoms/diseases', {
            symptoms: this.state.positiveSymptoms,
            disease: disease
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => this.setState({
            message: "Successfully saved your response."
        }))
    }
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">WhatNext</h1>
                    <img src={logo} className="App-logo" alt="logo"/>
                </header>
                {!this.state.message && <div>

                    < SymptomsSummary
                        positiveSymptoms={this.state.positiveSymptoms}
                        negativeSymptoms={this.state.negativeSymptoms}
                        />
                        <SearchArea
                        symptoms={this.state.symptoms}
                        submitFilters={this.submitFilters.bind(this)}
                        />
                    {(this.state.positiveSymptoms.length >0 || this.state.negativeSymptoms.length>0) &&
                    <DiseasePredictor diseases={this.state.diseases}
                                      save={this.saveDiagnosis}
                    />
                    }
                </div>
            }
                {this.state.message != "" && <div style={{textAlign: 'center',
                    padding: '10px'}}>{this.state.message}</div>}
            </div>
        );
    }
}

export default App;
