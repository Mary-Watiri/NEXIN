import React from 'react'
import { ResponsivePie } from '@nivo/pie'
import { PieData as data } from '../Data/MockData'
import { Box } from '@mui/material'
function Pie() {
  return (
    <Box class="h-3/4 w-full p-7">
   <h1 className='text-slate-300  font-bold text-2xl'>Pie Chart</h1>
    <h3 className="text-emerald-500">To show the Profits and Losses</h3>
<ResponsivePie
        data={data}
        margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
        innerRadius={0.5}
        padAngle={0.7}
        cornerRadius={3}
        activeOuterRadiusOffset={8}
        borderWidth={1}
        borderColor={{
            from: 'color',
            modifiers: [
                [
                    'darker',
                    0.2
                ]
            ]
        }}
        arcLinkLabelsSkipAngle={10}
        arcLinkLabelsTextColor="#333333"
        arcLinkLabelsThickness={2}
        arcLinkLabelsColor={{ from: 'color' }}
        arcLabelsSkipAngle={10}
        arcLabelsTextColor={{
            from: 'color',
            modifiers: [
                [
                    'darker',
                    2
                ]
            ]
        }}
        defs={[
            {
                id: 'dots',
                type: 'patternDots',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                size: 4,
                padding: 1,
                stagger: true
            },
            {
                id: 'lines',
                type: 'patternLines',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                rotation: -45,
                lineWidth: 6,
                spacing: 10
            }
        ]}
        fill={[
            {
                match: {
                    id: 'January'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'February'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'March'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'April'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'May'
                },
                id: 'lines'
            },
            {
                match: {
                    id: 'June'
                },
                id: 'lines'
            },
            {
                match: {
                    id: 'July'
                },
                id: 'lines'
            }
           
        ]}
        legends={[
            {
                anchor: 'bottom',
                direction: 'row',
                justify: false,
                translateX: 0,
                translateY: 56,
                itemsSpacing: 0,
                itemWidth: 100,
                itemHeight: 18,
                itemTextColor: '#999',
                itemDirection: 'left-to-right',
                itemOpacity: 1,
                symbolSize: 18,
                symbolShape: 'circle',
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemTextColor: '#000'
                        }
                    }
                ]
            }
        ]}
    />
    </Box>
   
    
  )
}

export default Pie
