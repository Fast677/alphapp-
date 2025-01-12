import React from 'react';
import { render, screen } from '@testing-library/react';
import ReusableComponent from './ReusableComponent';

describe('ReusableComponent', () => {
    it('renders without crashing', () => {
        render(<ReusableComponent />);
        expect(screen.getByText(/some text/i)).toBeInTheDocument();
    });

    it('displays the correct props', () => {
        render(<ReusableComponent propName="test" />);
        expect(screen.getByText(/test/i)).toBeInTheDocument();
    });
});